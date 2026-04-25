import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

main_htm = """<html><body><title>Meraki Store</title>
<center>
<img src="L2UI_CH3.onscrmsg_pattern01_1" width=300 height=32><br>
<font color="LEVEL">Welcome to the Meraki Store!</font><br>
I have everything you need to start your journey.<br>
<img src="L2UI.SquareGray" width=250 height=1><br>
<button value="Weapons" action="bypass -h npc_%objectId%_Chat 1" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="Armors" action="bypass -h npc_%objectId%_Chat 2" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="Jewelry" action="bypass -h npc_%objectId%_Chat 3" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="Consumables" action="bypass -h npc_%objectId%_Chat 4" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<img src="L2UI.SquareGray" width=250 height=1><br>
<button value="Donation Shop" action="bypass -h npc_%objectId%_multisell 90005" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="Event Shop" action="bypass -h npc_%objectId%_multisell 90006" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
</center>
</body></html>"""
write_file('server_data/game/data/html/merchant/50009.htm', main_htm)

weapons_htm = """<html><body><title>Meraki Store - Weapons</title>
<center>
<font color="LEVEL">Weapons</font><br><br>
<button value="No-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="D-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="C-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="B-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-1.htm', weapons_htm)

armors_htm = """<html><body><title>Meraki Store - Armors</title>
<center>
<font color="LEVEL">Armors</font><br><br>
<button value="No-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="D-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="C-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="B-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-2.htm', armors_htm)

jewels_htm = """<html><body><title>Meraki Store - Jewelry</title>
<center>
<font color="LEVEL">Jewelry</font><br><br>
<button value="All Grades (NG to B)" action="bypass -h npc_%objectId%_multisell 90003" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-3.htm', jewels_htm)

consumables_htm = """<html><body><title>Meraki Store - Consumables</title>
<center>
<font color="LEVEL">Consumables</font><br><br>
<button value="Soulshots / Spiritshots" action="bypass -h npc_%objectId%_multisell 90004" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<button value="Potions & Scrolls" action="bypass -h npc_%objectId%_multisell 90004" width=130 height=21 back="L2UI_CH3.bigbutton_down" fore="L2UI_CH3.bigbutton"><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" width=70 height=21 back="L2UI_CH3.smallbutton_down" fore="L2UI_CH3.smallbutton"><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-4.htm', consumables_htm)

print("HTMLs repared using safe <br> structure instead of tables.")
