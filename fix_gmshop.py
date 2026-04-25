import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

# 1. Fix NPC Display ID
npc_xml = """<?xml version="1.0" encoding="UTF-8"?>
<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../../../xsd/npcs.xsd">
	<npc id="50009" displayId="30084" name="Meraki Store" usingServerSideName="true" title="GM Shop" usingServerSideTitle="true" type="Merchant">
		<collision>
			<radius normal="8" />
			<height normal="23" />
		</collision>
	</npc>
</list>
"""
write_file('server_data/game/data/stats/npcs/custom/GMShop.xml', npc_xml)

# 2. Fix HTMLs (using proper Tables for alignment)
main_htm = """<html><body><title>Meraki Store</title>
<center>
<img src="L2UI_CH3.onscrmsg_pattern01_1" width=300 height=32><br>
<font color="LEVEL">Welcome to the Meraki Store!</font><br>
I have everything you need to start your journey.<br>
<img src="L2UI.SquareGray" width=250 height=1><br>
<table width=250>
<tr><td align=center><button value="Weapons" action="bypass -h npc_%objectId%_Chat 1" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="Armors" action="bypass -h npc_%objectId%_Chat 2" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="Jewelry" action="bypass -h npc_%objectId%_Chat 3" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="Consumables" action="bypass -h npc_%objectId%_Chat 4" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
</table>
<img src="L2UI.SquareGray" width=250 height=1><br>
<table width=250>
<tr><td align=center><button value="Donation Shop" action="bypass -h npc_%objectId%_multisell 90005" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="Event Shop" action="bypass -h npc_%objectId%_multisell 90006" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
</table>
</center>
</body></html>"""
write_file('server_data/game/data/html/merchant/50009.htm', main_htm)

weapons_htm = """<html><body><title>Meraki Store - Weapons</title>
<center>
<font color="LEVEL">Weapons</font><br><br>
<table width=250>
<tr><td align=center><button value="No-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="D-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="C-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="B-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"></td></tr>
</table>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-1.htm', weapons_htm)

armors_htm = """<html><body><title>Meraki Store - Armors</title>
<center>
<font color="LEVEL">Armors</font><br><br>
<table width=250>
<tr><td align=center><button value="No-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="D-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="C-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="B-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"></td></tr>
</table>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-2.htm', armors_htm)

jewels_htm = """<html><body><title>Meraki Store - Jewelry</title>
<center>
<font color="LEVEL">Jewelry</font><br><br>
<table width=250>
<tr><td align=center><button value="All Grades (NG to B)" action="bypass -h npc_%objectId%_multisell 90003" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"></td></tr>
</table>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-3.htm', jewels_htm)

consumables_htm = """<html><body><title>Meraki Store - Consumables</title>
<center>
<font color="LEVEL">Consumables</font><br><br>
<table width=250>
<tr><td align=center><button value="Soulshots / Spiritshots" action="bypass -h npc_%objectId%_multisell 90004" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><button value="Potions & Scrolls" action="bypass -h npc_%objectId%_multisell 90004" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"></td></tr>
<tr><td align=center><br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"></td></tr>
</table>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-4.htm', consumables_htm)

# 3. Add NPCS restriction to all Multisells
import glob
for ms_file in glob.glob('server_data/game/data/multisell/9000*.xml'):
    with open(ms_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if npcs node already exists
    if '<npcs>' not in content:
        # Insert <npcs><npc>50009</npc></npcs> right after <list ...>
        content = content.replace('>', '>\n\t<npcs><npc>50009</npc></npcs>', 1)
        
        with open(ms_file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Fixes applied: HTML formatting, NPC Display ID, and Multisell NPCS restriction.")
