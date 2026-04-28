import os
import re

# Configuración
SERVER_ITEMS = r'f:\Programador GS\L2 Meraki\server_data\game\data\stats\items\custom\crack_shot_skins.xml'
MULTISELL = r'f:\Programador GS\L2 Meraki\server_data\game\data\multisell\custom\900010.xml'
OUTPUT_DAT = r'f:\Programador GS\L2 Meraki\tools\SKINS_DAT_FINAL.txt'
TOOLS_DIR = r'f:\Programador GS\L2 Meraki\tools'

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../../../xsd/items.xsd">
	<item id="9910" name="Crack Shot Blue Outfit" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="CLOTH" /></item>
	<item id="9911" name="Crack Shot Gold Outfit" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="CLOTH" /></item>
	<item id="9912" name="Crack Shot Pink Outfit" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="CLOTH" /></item>
	<item id="9913" name="Crack Shot Red Outfit" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="CLOTH" /></item>
	<item id="9914" name="Crack Shot Skull Outfit" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="CLOTH" /></item>
	<item id="9930" name="Japan General Costume" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="STEEL" /></item>
	<item id="9931" name="White Knight Costume" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="STEEL" /></item>
	<item id="9933" name="Cat Costume" type="Armor"><set name="icon" val="icon.armor_t91_u_i00" /><set name="default_action" val="EQUIP" /><set name="bodypart" val="onepiece" /><set name="material" val="CLOTH" /></item>
</list>"""

multisell_content = """<?xml version='1.0' encoding='utf-8'?>
<list>
	<item><ingredient id="4037" count="10" /><production id="9910" count="1" /></item>
	<item><ingredient id="4037" count="10" /><production id="9911" count="1" /></item>
	<item><ingredient id="4037" count="10" /><production id="9912" count="1" /></item>
	<item><ingredient id="4037" count="10" /><production id="9913" count="1" /></item>
	<item><ingredient id="4037" count="10" /><production id="9914" count="1" /></item>
	<item><ingredient id="4037" count="15" /><production id="9930" count="1" /></item>
	<item><ingredient id="4037" count="15" /><production id="9931" count="1" /></item>
	<item><ingredient id="4037" count="15" /><production id="9933" count="1" /></item>
</list>"""

with open(SERVER_ITEMS, 'w') as f: f.write(xml_content)
with open(MULTISELL, 'w') as f: f.write(multisell_content)

crack_dat = os.path.join(TOOLS_DIR, 'CrackShot_FIXED', 'Crack Shot (Interlude)', 'DAT.txt')
if os.path.exists(crack_dat):
    with open(crack_dat, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        content = re.sub(r'LineageCustom_CrackShot[A-Za-z]+_L2Prague\.icons\.[a-z0-9_]+', 'icon.armor_t91_u_i00', content)
        with open(OUTPUT_DAT, 'w') as out: out.write("--- CRACK SHOT LINES ---\n" + content)

print("Restauracion completada.")
