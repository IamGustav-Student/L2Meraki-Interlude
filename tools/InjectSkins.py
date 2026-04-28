import os

def inject_skins():
    # Rutas
    armor_file = r'f:\Programador GS\L2 Meraki\tools\armorgrp_test.txt'
    itemname_file = r'f:\Programador GS\L2 Meraki\tools\itemname_master.txt'
    
    # IDs a limpiar para evitar duplicados
    ids_to_clean = set(range(9810, 9815)) | set(range(9910, 9915)) | set(range(9930, 9940))
    
    # --- PROCESAR ARMORGRP ---
    try:
        with open(armor_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(armor_file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
    
    header = lines[0]
    new_armor_lines = [header]
    for line in lines[1:]:
        parts = line.split('\t')
        if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) not in ids_to_clean:
            new_armor_lines.append(line)
            
    # Función para crear línea de armorgrp con formato Interlude (1 modelo por raza)
    def make_armor_line(id, mesh, tex, icon):
        # Campos iniciales: 22 columnas
        line = f"1\t{id}\t0\t3\t7\t0\t0\tdropitems.drop_wedding_box_m00\t\t\t{tex}\t\t\t{icon}\t{icon}\t{icon}\t{icon}\t{icon}\t4294967295\t500\t19\t0\t0\t10\t"
        
        # Cada raza (14 razas) x 21 campos = 294 columnas
        # Un campo de raza tiene: cntm, m[0-3], cntt, t[0-3], add_cntm, add_m[0-3], add_cntt, add_t[0-3]
        mesh_part = f"1\t{mesh}\t\t\t\t1\t{tex}\t\t\t\t0\t\t\t\t\t0\t\t\t\t\t"
        line += mesh_part * 14
        
        # Campos finales: 16 columnas aprox.
        # Unknown_MT_cntm... item_sound... UNK_2... pdef... mpbonus
        line += "0\t\t0\t\t0\t\t0\t\t0\t\t0\t\tLineageEffect.p_u002_a\t4\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.armor_leather_2\tItemSound.armor_leather_8\tItemSound.itemdrop_etc_book\tItemSound.itemequip_armor_cloth\t1\t0\t0\t0\t0\t0\t0\t0\n"
        return line

    # Inyectar nuevas skins
    # CRACK SHOT PACK
    new_armor_lines.append(make_armor_line(9910, "LineageCustom_CrackShotBlue_L2Prague.CrackShot_MFighter_m010", "LineageCustom_CrackShotBlue_L2Prague.run_000.armorTex", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9911, "LineageCustom_CrackShotGold_L2Prague.CrackShot_MFighter_m010", "LineageCustom_CrackShotGold_L2Prague.run_000.armorTex", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9912, "LineageCustom_CrackShotPink_L2Prague.CrackShot_MFighter_m010", "LineageCustom_CrackShotPink_L2Prague.run_000.armorTex", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9913, "LineageCustom_CrackShotRed_L2Prague.CrackShot_MFighter_m010", "LineageCustom_CrackShotRed_L2Prague.run_000.armorTex", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9914, "LineageCustom_CrackShotSkull_L2Prague.CrackShot_MFighter_m010", "LineageCustom_CrackShotSkull_L2Prague.run_000.armorTex", "icon.armor_t91_u_i00"))
    
    # OTROS COSTUMES
    new_armor_lines.append(make_armor_line(9930, "JapanGeneral.JapanGeneral_mfighter", "dropitemstex.drop_wedding_box_t00", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9931, "RaccoonCustom05.MFighter_bkt2_m010", "RaccoonCustom05.white_knight_suit", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9932, "RaccoonCustom04.MFighter_bkt1_m010", "RaccoonCustom04.valkyrie_suit", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9933, "CatMesh.Cat_mfighter", "dropitemstex.drop_wedding_box_t00", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9934, "halloween_skeleton_m00", "helloween_tex.helloween_skeleton", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9935, "ninja_m00", "ninja_tex.ninja_suit", "icon.armor_t91_u_i00"))
    new_armor_lines.append(make_armor_line(9936, "zaken_pirate_m00", "zaken_tex.zaken_pirate_suit", "icon.armor_t91_u_i00"))

    with open(r'f:\Programador GS\L2 Meraki\tools\temp_armorgrp_final.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_armor_lines)

    # --- PROCESAR ITEMNAME ---
    try:
        with open(itemname_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(itemname_file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
    
    new_item_lines = [lines[0]]
    for line in lines[1:]:
        parts = line.split('\t')
        if len(parts) > 0 and parts[0].isdigit() and int(parts[0]) not in ids_to_clean:
            new_item_lines.append(line)
            
    # Agregar todos los nombres
    skins = {
        9910: "Crack Shot Blue Outfit",
        9911: "Crack Shot Gold Outfit",
        9912: "Crack Shot Pink Outfit",
        9913: "Crack Shot Red Outfit",
        9914: "Crack Shot Skull Outfit",
        9930: "Japan General Costume",
        9931: "White Knight Costume",
        9932: "Valkyrie Costume",
        9933: "Cat Costume",
        9934: "Halloween Skeleton",
        9935: "Ninja Skin",
        9936: "Zaken Skin"
    }
    for id, name in skins.items():
        # Formato exacto 13 columnas: id, name, add_name, desc, popup, set_ids, set_bonus, set_extra_id, set_extra_desc, unk0, unk1, enchant_val, enchant_desc
        # IMPORTANTE: Usamos \\0 para que se escriba el texto literal \0
        line = f"{id}\t{name}\ta,\ta,{name}.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n"
        new_item_lines.append(line)

    import codecs
    with codecs.open(r'f:\Programador GS\L2 Meraki\tools\temp_itemname_final.txt', 'w', 'utf-16') as f:
        # Escribir el BOM manualmente si es necesario, aunque codecs.open con 'utf-16' lo incluye por defecto
        f.writelines(new_item_lines)

    print("Archivos temporales generados con exito.")

if __name__ == '__main__':
    inject_skins()
