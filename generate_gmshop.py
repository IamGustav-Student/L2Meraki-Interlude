import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

# 1. NPC Definition
npc_xml = """<?xml version="1.0" encoding="UTF-8"?>
<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../../../xsd/npcs.xsd">
	<npc id="50009" displayId="32120" name="Meraki Store" usingServerSideName="true" title="GM Shop" usingServerSideTitle="true" type="Merchant">
		<collision>
			<radius normal="8" />
			<height normal="23" />
		</collision>
	</npc>
</list>
"""
write_file('server_data/game/data/stats/npcs/custom/GMShop.xml', npc_xml)

# 2. Main HTML
main_htm = """<html><body><title>Meraki Store</title>
<center>
<img src="L2UI_CH3.onscrmsg_pattern01_1" width=300 height=32><br>
<font color="LEVEL">Welcome to the Meraki Store!</font><br>
I have everything you need to start your journey.<br>
<img src="L2UI.SquareGray" width=250 height=1><br>
<button value="Weapons" action="bypass -h npc_%objectId%_Chat 1" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="Armors" action="bypass -h npc_%objectId%_Chat 2" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="Jewelry" action="bypass -h npc_%objectId%_Chat 3" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="Consumables" action="bypass -h npc_%objectId%_Chat 4" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<img src="L2UI.SquareGray" width=250 height=1><br>
<button value="Donation Shop" action="bypass -h npc_%objectId%_multisell 90005" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="Event Shop" action="bypass -h npc_%objectId%_multisell 90006" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
</center>
</body></html>"""
write_file('server_data/game/data/html/merchant/50009.htm', main_htm)

# Weapons HTML
weapons_htm = """<html><body><title>Meraki Store - Weapons</title>
<center>
<font color="LEVEL">Weapons</font><br>
<button value="No-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="D-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="C-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="B-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton">
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-1.htm', weapons_htm)

# Armors HTML
armors_htm = """<html><body><title>Meraki Store - Armors</title>
<center>
<font color="LEVEL">Armors</font><br>
<button value="No-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="D-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="C-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="B-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton">
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-2.htm', armors_htm)

# Jewelry HTML
jewels_htm = """<html><body><title>Meraki Store - Jewelry</title>
<center>
<font color="LEVEL">Jewelry</font><br>
<button value="All Grades (NG to B)" action="bypass -h npc_%objectId%_multisell 90003" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton">
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-3.htm', jewels_htm)

# Consumables HTML
consumables_htm = """<html><body><title>Meraki Store - Consumables</title>
<center>
<font color="LEVEL">Consumables</font><br>
<button value="Soulshots / Spiritshots" action="bypass -h npc_%objectId%_multisell 90004" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<button value="Potions & Scrolls" action="bypass -h npc_%objectId%_multisell 90004" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton">
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton">
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-4.htm', consumables_htm)

# Multisells
ms_template = '''<?xml version="1.0" encoding="UTF-8"?>
<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../../xsd/multisell.xsd">
{items}
</list>'''

def make_ms_item(item_idx, price_id, price_count, prod_id, prod_count=1):
    return f'''	<item id="{item_idx}">
		<ingredient id="{price_id}" count="{price_count}" />
		<production id="{prod_id}" count="{prod_count}" />
	</item>'''

# 90001 Weapons (Sample Sword of Revolution, Stormbringer, etc)
wep_items = [
    (1, 57, 150000, 73),  # Broadsword
    (2, 57, 1000000, 122), # Sword of Revolution
    (3, 57, 5000000, 74), # Stormbringer
    (4, 57, 12000000, 75) # Great Sword (B)
]
wep_xml = ms_template.format(items='\n'.join(make_ms_item(*i) for i in wep_items))
write_file('server_data/game/data/multisell/90001.xml', wep_xml)

# 90002 Armors
arm_items = [
    (1, 57, 50000, 421), # Wooden Breastplate
    (2, 57, 300000, 425), # Mithril Tunic
    (3, 57, 1500000, 352), # Composite Armor
    (4, 57, 5000000, 2377) # Zubei's Breastplate (B)
]
arm_xml = ms_template.format(items='\n'.join(make_ms_item(*i) for i in arm_items))
write_file('server_data/game/data/multisell/90002.xml', arm_xml)

# 90003 Jewels
jewel_items = [
    (1, 57, 20000, 843), # Earring of Wisdom
    (2, 57, 80000, 852), # Elven Earring
    (3, 57, 500000, 855), # Aquestone Ring
    (4, 57, 1500000, 858) # Ring of Binding
]
jewel_xml = ms_template.format(items='\n'.join(make_ms_item(*i) for i in jewel_items))
write_file('server_data/game/data/multisell/90003.xml', jewel_xml)

# 90004 Consumables
cons_items = [
    (1, 57, 100, 1463), # Soulshot D
    (2, 57, 200, 1464), # Soulshot C
    (3, 57, 400, 1465), # Soulshot B
    (4, 57, 100, 3947), # BSS D
    (5, 57, 200, 3948), # BSS C
    (6, 57, 400, 3949), # BSS B
    (7, 57, 500, 1539), # Greater Healing Potion
    (8, 57, 1000, 736) # Scroll of Escape
]
cons_xml = ms_template.format(items='\n'.join(make_ms_item(*i) for i in cons_items))
write_file('server_data/game/data/multisell/90004.xml', cons_xml)

# 90005 Donation (Coin of Luck id 4037)
don_items = [
    (1, 4037, 50, 5249), # Meraki VIP
    (2, 4037, 15, 8936) # Romantic Chapeau
]
don_xml = ms_template.format(items='\n'.join(make_ms_item(*i) for i in don_items))
write_file('server_data/game/data/multisell/90005.xml', don_xml)

# 90006 Event (Glittering Medal id 3434)
evt_items = [
    (1, 3434, 1000, 8546), # Party Hat
    (2, 3434, 5000, 6622) # Agathion
]
evt_xml = ms_template.format(items='\n'.join(make_ms_item(*i) for i in evt_items))
write_file('server_data/game/data/multisell/90006.xml', evt_xml)


# Generate Spawns
import xml.etree.ElementTree as ET

gk_ids = {
    '31964', '31698', '31699', '31320', '31275', '30836', '30848', '30899', '30727', 
    '30540', '30576', '30483', '30320', '30233', '30256', '30146', '30162', '30177', 
    '30006', '30059', '30080'
}

spawns_dir = 'server_data/game/data/spawns'
new_spawns = []

for root, dirs, files in os.walk(spawns_dir):
    for file in files:
        if file.endswith('.xml'):
            filepath = os.path.join(root, file)
            try:
                tree = ET.parse(filepath)
                xml_root = tree.getroot()
                for spawn in xml_root.findall('.//spawn'):
                    for npc in spawn.findall('npc'):
                        if npc.get('id') in gk_ids:
                            # offset by -50 x, -50 y so it sits on the opposite side of the Buffer
                            x = int(npc.get('x')) - 50
                            y = int(npc.get('y')) - 50
                            z = npc.get('z')
                            heading = npc.get('heading')
                            new_spawns.append(f'		<npc id="50009" x="{x}" y="{y}" z="{z}" heading="{heading}" respawnDelay="5" /> <!-- Meraki GMShop near GK {npc.get("id")} -->')
            except Exception as e:
                pass 

xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<list enabled="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../../xsd/spawns.xsd">
	<spawn name="MerakiGMShop_Global">
'''
xml_content += '\n'.join(new_spawns)
xml_content += '''
	</spawn>
</list>
'''
write_file('server_data/game/data/spawns/Others/MerakiGMShop.xml', xml_content)
print("GM Shop generated successfully! Multisells, HTMLs, and Spawns created.")
