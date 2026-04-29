import os
import subprocess

# CONFIGURACION
TOOLS_DIR = r"f:\Programador GS\L2 Meraki\tools"
SYSTEM_DIR = r"f:\Programador GS\L2 Meraki\system_master\system"

# HERRAMIENTAS
L2ASM = os.path.join(TOOLS_DIR, "l2asm.exe")
L2DISASM = os.path.join(TOOLS_DIR, "l2disasm.exe")
L2ENCDEC = os.path.join(TOOLS_DIR, "l2encdec.exe")

def inject_and_compile():
    # 1. PROCESAR ITEMNAME-E
    print("Procesando itemname-e...")
    with open(os.path.join(TOOLS_DIR, "itemname-e.txt"), "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    # Limpiar cabecera (obligatorio para l2asm si el DDF no la ignora bien)
    data_lines = [l for l in lines if l[0].isdigit()]
    
    # Añadir nuevas
    data_lines.append("60000\tSamurai Outfit\ta,Samurai Skin\\0\ta,Increases appearance by applying Samurai Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    data_lines.append("60001\tHalloween Outfit\ta,Halloween Skin\\0\ta,Increases appearance by applying Halloween Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    data_lines.append("60002\tNinja Outfit\ta,Ninja Skin\\0\ta,Increases appearance by applying Ninja Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    data_lines.append("60003\tZaken Outfit\ta,Zaken Skin\\0\ta,Increases appearance by applying Zaken Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    
    with open(os.path.join(TOOLS_DIR, "itemname-e_ready.txt"), "w", encoding="utf-8") as f:
        f.writelines(data_lines)

    # 2. PROCESAR ARMORGRP
    print("Procesando armorgrp...")
    with open(os.path.join(TOOLS_DIR, "armorgrp.txt"), "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    data_lines_armor = [l for l in lines if l.startswith("1\t")]
    
    def make_armor_line(id, mesh, tex, icon):
        base = f"1\t{id}\t0\t3\t7\t0\t0\tdropitems.drop_mfighter_m001_t02_u_m00\t\t\tMFighter.MFighter_m001_t02_u\t\t\t{icon}\t{icon}\t{icon}\t{icon}\t{icon}\t4294967295\t500\t19\t0\t0\t10\t"
        # 14 Razas: cntm=1, mesh, cntt=1, tex, add_cntm=0, add_cntt=0
        mesh_block = f"1\t{mesh}\t1\t{tex}\t0\t0\t"
        final = "0\t0\t0\t0\t0\t0\tLineageEffect.p_u002_a\t4\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.itemdrop_etc_book\tItemSound.itemequip_armor_cloth\t1\t0\t0\t0\t0\t0\t0\t0\n"
        return base + (mesh_block * 14) + final

    data_lines_armor.append(make_armor_line(60000, "JapanGeneral.JapanGeneral_mfighter", "dropitemstex.drop_wedding_box_t00", "icon.armor_t91_u_i00"))
    data_lines_armor.append(make_armor_line(60001, "halloween_skeleton_m00", "helloween_tex.helloween_skeleton", "icon.etc_skeleton_m_i00"))
    data_lines_armor.append(make_armor_line(60002, "SHEV_SingleMeshFigher", "SHEV_SingleMeshTex.ninja_suit", "icon.armor_t89_u_i00"))
    data_lines_armor.append(make_armor_line(60003, "zaken_pirate_m00", "zaken_tex.zaken_pirate_suit", "icon.etc_zaken_mask_i00"))

    with open(os.path.join(TOOLS_DIR, "armorgrp_ready.txt"), "w", encoding="utf-8") as f:
        f.writelines(data_lines_armor)

    # 3. COMPILAR (Usando RAW DATs primero)
    print("Ensamblando DATs...")
    subprocess.run(f'"{L2ASM}" -d "{os.path.join(TOOLS_DIR, "itemname-e.ddf")}" "{os.path.join(TOOLS_DIR, "itemname-e_ready.txt")}" itemname-e_raw.dat', shell=True, cwd=TOOLS_DIR)
    subprocess.run(f'"{L2ASM}" -d "{os.path.join(TOOLS_DIR, "armorgrp.ddf")}" "{os.path.join(TOOLS_DIR, "armorgrp_ready.txt")}" armorgrp_raw.dat', shell=True, cwd=TOOLS_DIR)
    
    # 4. ENCRIPTAR PARA EL JUEGO
    if os.path.exists(os.path.join(TOOLS_DIR, "itemname-e_raw.dat")):
        print("Encriptando itemname-e...")
        subprocess.run(f'"{L2ENCDEC}" -e 413 itemname-e_raw.dat "{os.path.join(SYSTEM_DIR, "itemname-e.dat")}"', shell=True, cwd=TOOLS_DIR)
    
    if os.path.exists(os.path.join(TOOLS_DIR, "armorgrp_raw.dat")):
        print("Encriptando armorgrp...")
        subprocess.run(f'"{L2ENCDEC}" -e 413 armorgrp_raw.dat "{os.path.join(SYSTEM_DIR, "armorgrp.dat")}"', shell=True, cwd=TOOLS_DIR)
    
    print("\n--- PROCESO AUTOMATICO FINALIZADO ---")

if __name__ == "__main__":
    inject_and_compile()
