import os
import subprocess

# RUTA BASE
TOOLS_DIR = r"f:\Programador GS\L2 Meraki\tools"
SYSTEM_DIR = r"f:\Programador GS\L2 Meraki\system_master\system"

# HERRAMIENTAS
L2ASM = os.path.join(TOOLS_DIR, "l2asm.exe")
L2DISASM = os.path.join(TOOLS_DIR, "l2disasm.exe")

def process_dat(file_name, ddf_name, new_lines_func):
    dat_path = os.path.join(SYSTEM_DIR, f"{file_name}.dat")
    txt_path = os.path.join(TOOLS_DIR, f"{file_name}.txt")
    ddf_path = os.path.join(TOOLS_DIR, f"{ddf_name}.ddf")
    
    print(f"--- PROCESANDO {file_name}.dat ---")
    
    # 1. Desensamblar
    cmd_dis = f'"{L2DISASM}" -d "{ddf_path}" "{dat_path}" "{txt_path}"'
    subprocess.run(cmd_dis, shell=True)
    
    if not os.path.exists(txt_path):
        print(f"Error: No se pudo desensamblar {file_name}")
        return

    # 2. Leer y Modificar
    with open(txt_path, 'r', encoding='utf-16') as f:
        lines = f.readlines()
    
    # Limpiar IDs 60000+ si ya existen
    new_lines = [lines[0]]
    for line in lines[1:]:
        parts = line.split('\t')
        if parts[0].isdigit() and int(parts[0]) >= 60000:
            continue
        new_lines.append(line)
        
    # Añadir nuevas
    new_lines.extend(new_lines_func())
    
    with open(txt_path, 'w', encoding='utf-16') as f:
        f.writelines(new_lines)
        
    # 3. Ensamblar
    cmd_asm = f'"{L2ASM}" -d "{ddf_path}" "{txt_path}" "{dat_path}"'
    subprocess.run(cmd_asm, shell=True)
    print(f"Exito: {file_name}.dat actualizado.")

def get_armor_lines():
    def make_line(id, mesh, tex, icon):
        # Estructura simplificada para inyeccion rapida en Interlude
        base = f"1\t{id}\t0\t3\t7\t0\t0\tdropitems.drop_wedding_box_m00\t\t\t{tex}\t\t\t{icon}\t{icon}\t{icon}\t{icon}\t{icon}\t4294967295\t500\t19\t0\t0\t10\t"
        mesh_block = f"1\t{mesh}\t\t\t\t1\t{tex}\t\t\t\t0\t\t\t\t\t0\t\t\t\t\t"
        final = "0\t\t0\t\t0\t\t0\t\t0\t\t0\t\tLineageEffect.p_u002_a\t4\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.itemdrop_etc_book\tItemSound.itemequip_armor_cloth\t1\t0\t0\t0\t0\t0\t0\t0\n"
        return base + (mesh_block * 14) + final

    return [
        make_line(60000, "JapanGeneral.JapanGeneral_mfighter", "dropitemstex.drop_wedding_box_t00", "icon.armor_t91_u_i00"),
        make_line(60001, "halloween_fighter_m00", "helloween_tex.helloween_skeleton", "icon.etc_skeleton_m_i00"),
        make_line(60002, "ninja_m00", "ninja_tex.ninja_suit", "icon.armor_t89_u_i00"),
        make_line(60003, "zaken_pirate_m00", "zaken_tex.zaken_pirate_suit", "icon.etc_zaken_mask_i00")
    ]

def get_itemname_lines():
    return [
        f"60000\tSamurai Outfit\ta,\ta,Increases appearance by applying Samurai Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n",
        f"60001\tHalloween Outfit\ta,\ta,Increases appearance by applying Halloween Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n",
        f"60002\tNinja Outfit\ta,\ta,Increases appearance by applying Ninja Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n",
        f"60003\tZaken Outfit\ta,\ta,Increases appearance by applying Zaken Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n"
    ]

if __name__ == "__main__":
    process_dat("armorgrp", "armorgrp", get_armor_lines)
    process_dat("itemname-e", "itemname-e", get_itemname_lines)
