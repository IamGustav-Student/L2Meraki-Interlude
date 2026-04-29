import struct
import os
import subprocess

TOOLS_DIR = r"f:\Programador GS\L2 Meraki\tools"
SYSTEM_DIR = r"f:\Programador GS\L2 Meraki\system_master\system"
L2ENCDEC = os.path.join(TOOLS_DIR, "l2encdec.exe")

def binary_inject():
    print("Iniciando inyeccion binaria (Intento 2)...")
    
    # Generar DDF expandida sin REP
    ddf_parts = [
        'FS = "\\t";',
        'HEADER = 0;',
        'RECCNT = OFF;',
        '{',
        '    UINT tag; UINT id; UINT d1; UINT d2; UINT d3; UINT d4; UINT d5;',
        '    ASCF m1; ASCF m2; ASCF m3; ASCF t1; ASCF t2; ASCF t3;',
        '    ASCF ic[5];',
        '    UINT du; UINT w; UINT m; UINT c; UINT u1; UINT b;'
    ]
    
    # 14 razas
    for i in range(14):
        ddf_parts.append(f'    UINT c1_{i}; ASCF b1_{i}; UINT c2_{i}; ASCF b2_{i}; UINT c3_{i}; ASCF b3_{i}; UINT c4_{i}; ASCF b4_{i};')
        
    ddf_parts.extend([
        '    UINT f1; ASCF f2; UINT f3; ASCF f4; UINT f5; ASCF f6; UINT f7; ASCF f8; UINT f9; ASCF f10; UINT f11; ASCF f12;',
        '    ASCF a1; UINT s1; ASCF s2[s1]; ASCF s3; ASCF s4;',
        '    UINT u2; UINT u3; UINT a2; UINT c2; UINT am; UINT p; UINT md; UINT mp;',
        '}'
    ])
    
    with open(os.path.join(TOOLS_DIR, "simple.ddf"), "w") as f:
        f.write("\n".join(ddf_parts))
        
    # Usar las 4 lineas de las skins
    with open(os.path.join(TOOLS_DIR, "armorgrp_ready.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    skin_lines = [l for l in lines if l.startswith("1\t6000")]
    
    # Limpiar las lineas para que coincidan EXACTAMENTE con la DDF simple
    # En la DDF simple, tenemos:
    # 7 UINTs, 6 ASCFs (drop), 5 ASCFs (icon), 6 UINTs (stats), 14*8 campos (razas), etc.
    # Vamos a procesar cada linea para asegurar que los campos vacios sean tratados como cadenas vacias
    
    clean_skin_lines = []
    for line in skin_lines:
        parts = line.strip().split('\t')
        # Rellenar hasta asegurar que no hay campos nulos que rompan l2asm
        while len(parts) < 150: # Suficiente para cubrir los campos
            parts.append("")
        clean_skin_lines.append("\t".join(parts) + "\n")

    with open(os.path.join(TOOLS_DIR, "skins_only.txt"), "w", encoding="utf-8") as f:
        f.writelines(clean_skin_lines)
        
    # Intentar compilar SOLO las skins
    print("Compilando bloque de skins...")
    subprocess.run(f'"{os.path.join(TOOLS_DIR, "l2asm.exe")}" -d simple.ddf skins_only.txt skins.bin', shell=True, cwd=TOOLS_DIR)
    
    if not os.path.exists(os.path.join(TOOLS_DIR, "skins.bin")):
        print("Error: Fallo en l2asm. Probando metodo alternativo...")
        return

    # 2. Leer y Modificar
    with open(os.path.join(TOOLS_DIR, "dec-armorgrp.dat"), "rb") as f:
        original_data = bytearray(f.read())
        
    count = struct.unpack("<I", original_data[0:4])[0]
    new_count = count + len(clean_skin_lines)
    original_data[0:4] = struct.pack("<I", new_count)
    
    with open(os.path.join(TOOLS_DIR, "skins.bin"), "rb") as f:
        skins_data = f.read()
    
    with open(os.path.join(TOOLS_DIR, "final_armorgrp_raw.dat"), "wb") as f:
        f.write(original_data + skins_data)
        
    print("Encriptando...")
    subprocess.run(f'"{L2ENCDEC}" -e 413 final_armorgrp_raw.dat "{os.path.join(SYSTEM_DIR, "armorgrp.dat")}"', shell=True, cwd=TOOLS_DIR)
    print("¡LISTO! Inyeccion completada.")

if __name__ == "__main__":
    binary_inject()
