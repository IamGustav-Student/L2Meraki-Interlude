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
    # itemname-e.txt es UTF-16 LE con BOM
    try:
        with open(os.path.join(TOOLS_DIR, "itemname-e.txt"), "r", encoding="utf-16") as f:
            lines = f.readlines()
    except UnicodeError:
        print("Error: itemname-e.txt no es UTF-16. Intentando con UTF-8...")
        with open(os.path.join(TOOLS_DIR, "itemname-e.txt"), "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    
    # Limpiar cabecera (solo líneas que empiecen con ID numérico)
    data_lines = [l for l in lines if l and l[0].isdigit()]
    
    # Añadir nuevas (Asegurar que terminen con \n)
    # Formato: id \t name \t add_name \t description \t popup \t ...
    data_lines.append("60000\tSamurai Outfit\ta,Samurai Skin\\0\ta,Increases appearance by applying Samurai Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    data_lines.append("60001\tHalloween Outfit\ta,Halloween Skin\\0\ta,Increases appearance by applying Halloween Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    data_lines.append("60002\tNinja Outfit\ta,Ninja Skin\\0\ta,Increases appearance by applying Ninja Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    data_lines.append("60003\tZaken Outfit\ta,Zaken Skin\\0\ta,Increases appearance by applying Zaken Skin.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n")
    
    # Guardar como UTF-8 sin BOM
    content = "".join(data_lines)
    with open(os.path.join(TOOLS_DIR, "itemname-e_ready.txt"), "w", encoding="utf-8") as f:
        f.write(content)

    # 2. PROCESAR ARMORGRP
    print("Procesando armorgrp...")
    with open(os.path.join(TOOLS_DIR, "armorgrp.txt"), "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    data_lines_armor = [l for l in lines if l and l[0].isdigit()]
    
    def make_armor_line(id, mesh, tex, icon):
        # Base: 24 campos
        base = f"1\t{id}\t0\t3\t7\t0\t0\tdropitems.drop_mfighter_m001_t02_u_m00\t\t\tMFighter.MFighter_m001_t02_u\t\t\t{icon}\t{icon}\t{icon}\t{icon}\t{icon}\t4294967295\t500\t19\t0\t0\t10\t"
        
        # 14 Razas: 20 campos cada una (Total 280)
        # cntm, m[4], cntt, t[4], add_cntm, add_m[4], add_cntt, add_t[4]
        race_block = f"1\t{mesh}\t\t\t\t1\t{tex}\t\t\t\t0\t\t\t\t\t0\t\t\t\t\t"
        all_races = race_block * 14
        
        # Special MTs (3 * 4 = 12 campos)
        special_mts = "0\t\t0\t\t" * 3
        
        # End: 16 campos
        # att_eff, sound_cnt, sound[4], drop, equip, unk2, unk3, type, crystal, avoid, pdef, mdef, mp
        final = "\t4\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.itemdrop_etc_book\tItemSound.itemequip_armor_cloth\t1\t0\t0\t0\t0\t0\t0\t0\n"
        
        return base + all_races + special_mts + final

    data_lines_armor.append(make_armor_line(60000, "JapanGeneral.JapanGeneral_mfighter", "dropitemstex.drop_wedding_box_t00", "icon.armor_t91_u_i00"))
    data_lines_armor.append(make_armor_line(60001, "halloween_skeleton_m00", "helloween_tex.helloween_skeleton", "icon.etc_skeleton_m_i00"))
    data_lines_armor.append(make_armor_line(60002, "SHEV_SingleMeshFigher", "SHEV_SingleMeshTex.ninja_suit", "icon.armor_t89_u_i00"))
    data_lines_armor.append(make_armor_line(60003, "zaken_pirate_m00", "zaken_tex.zaken_pirate_suit", "icon.etc_zaken_mask_i00"))

    with open(os.path.join(TOOLS_DIR, "armorgrp_ready.txt"), "w", encoding="utf-8") as f:
        f.writelines(data_lines_armor)

    # 3. COMPILAR (Limpiar temporales primero)
    print("Ensamblando DATs...")
    for tmp in ["itemname-e_raw.dat", "armorgrp_raw.dat"]:
        if os.path.exists(os.path.join(TOOLS_DIR, tmp)): os.remove(os.path.join(TOOLS_DIR, tmp))

    subprocess.run(f'"{L2ASM}" -d "{os.path.join(TOOLS_DIR, "itemname-e.ddf")}" "{os.path.join(TOOLS_DIR, "itemname-e_ready.txt")}" itemname-e_raw.dat', shell=True, cwd=TOOLS_DIR)
    subprocess.run(f'"{L2ASM}" -d "{os.path.join(TOOLS_DIR, "armorgrp.ddf")}" "{os.path.join(TOOLS_DIR, "armorgrp_ready.txt")}" armorgrp_raw.dat', shell=True, cwd=TOOLS_DIR)
    
    # 4. ENCRIPTAR PARA EL JUEGO
    def finalize_dat(raw_name, final_path):
        raw_path = os.path.join(TOOLS_DIR, raw_name)
        if os.path.exists(raw_path) and os.path.getsize(raw_path) > 1000:
            print(f"Encriptando {raw_name}...")
            subprocess.run(f'"{L2ENCDEC}" -e 413 {raw_name} "{final_path}"', shell=True, cwd=TOOLS_DIR)
            if os.path.exists(final_path):
                print(f"OK: {os.path.basename(final_path)} generado ({os.path.getsize(final_path)} bytes)")
        else:
            print(f"ERROR: {raw_name} no se generó correctamente o está vacío.")

    finalize_dat("itemname-e_raw.dat", os.path.join(SYSTEM_DIR, "itemname-e.dat"))
    finalize_dat("armorgrp_raw.dat", os.path.join(SYSTEM_DIR, "armorgrp.dat"))
    
    print("\n--- PROCESO AUTOMATICO FINALIZADO ---")

if __name__ == "__main__":
    inject_and_compile()
