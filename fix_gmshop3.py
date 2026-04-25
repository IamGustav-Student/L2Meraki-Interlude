import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

# The clean button textures from Scheme Buffer
BTN = 'width=134 height=21 back="L2UI_ch3.BigButton3_over" fore="L2UI_ch3.BigButton3"'
S_BTN = 'width=74 height=21 back="L2UI_ch3.smallbutton2_over" fore="L2UI_ch3.smallbutton2"'

main_htm = f"""<html><body><title>Meraki Store</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Welcome to the Meraki Store!</font><br>
I have everything you need to start your journey.<br>
<img src="L2UI.SquareGray" width=250 height=1><br><br>
<button value="Weapons" action="bypass -h npc_%objectId%_Chat 1" {BTN}><br>
<button value="Armors" action="bypass -h npc_%objectId%_Chat 2" {BTN}><br>
<button value="Jewelry" action="bypass -h npc_%objectId%_Chat 3" {BTN}><br>
<button value="Consumables" action="bypass -h npc_%objectId%_Chat 4" {BTN}><br><br>
<img src="L2UI.SquareGray" width=250 height=1><br><br>
<button value="Donation Shop" action="bypass -h npc_%objectId%_Chat 5" {BTN}><br>
<button value="Event Shop" action="bypass -h npc_%objectId%_Chat 6" {BTN}><br>
</center>
</body></html>"""
write_file('server_data/game/data/html/merchant/50009.htm', main_htm)

weapons_htm = f"""<html><body><title>Meraki Store - Weapons</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Weapons</font><br><br>
<button value="No-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" {BTN}><br>
<button value="D-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" {BTN}><br>
<button value="C-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" {BTN}><br>
<button value="B-Grade Weapons" action="bypass -h npc_%objectId%_multisell 90001" {BTN}><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" {S_BTN}><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-1.htm', weapons_htm)

armors_htm = f"""<html><body><title>Meraki Store - Armors</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Armors</font><br><br>
<button value="No-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" {BTN}><br>
<button value="D-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" {BTN}><br>
<button value="C-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" {BTN}><br>
<button value="B-Grade Armors" action="bypass -h npc_%objectId%_multisell 90002" {BTN}><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" {S_BTN}><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-2.htm', armors_htm)

jewels_htm = f"""<html><body><title>Meraki Store - Jewelry</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Jewelry</font><br><br>
<button value="All Grades (NG to B)" action="bypass -h npc_%objectId%_multisell 90003" {BTN}><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" {S_BTN}><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-3.htm', jewels_htm)

consumables_htm = f"""<html><body><title>Meraki Store - Consumables</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Consumables</font><br><br>
<button value="Soulshots & Spiritshots" action="bypass -h npc_%objectId%_multisell 90004" {BTN}><br>
<button value="Potions & Scrolls" action="bypass -h npc_%objectId%_multisell 90004" {BTN}><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" {S_BTN}><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-4.htm', consumables_htm)

don_htm = f"""<html><body><title>Meraki Store - Donation Shop</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Donation Shop</font><br><br>
<button value="Premium Items" action="bypass -h npc_%objectId%_multisell 90005" {BTN}><br>
<button value="Accessories" action="bypass -h npc_%objectId%_multisell 90005" {BTN}><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" {S_BTN}><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-5.htm', don_htm)

evt_htm = f"""<html><body><title>Meraki Store - Event Shop</title>
<center>
<img src="L2UI_CH3.herotower_deco" width=256 height=32><br>
<font color="LEVEL">Event Shop</font><br><br>
<button value="Event Rewards" action="bypass -h npc_%objectId%_multisell 90006" {BTN}><br>
<br><button value="Back" action="bypass -h npc_%objectId%_Chat 0" {S_BTN}><br>
</center></body></html>"""
write_file('server_data/game/data/html/merchant/50009-6.htm', evt_htm)

print("HTMLs regenerated with flawless BigButton3 textures and all sub-menus created.")
