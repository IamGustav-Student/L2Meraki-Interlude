import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

# Template strings
B_BTN = 'width=85 height=26 back="L2UI_ch3.BigButton2_over" fore="L2UI_ch3.BigButton2"'

# --- Main HTML ---
main_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<br>
<center><img src=L2UI.SquareGray width=150 height=1></center>
<td><img src="L2UI.SquareBlank" width=40 height=2></td>
<center><img src="L2UI.SquareGray" width=250 height=1></center>
<font color=3c3c3c>_________</font> <font color=ae9977>Meraki Store</font> <font color=3c3c3c>_________</font><br>
<table width=230>
<tr>
<td align=center><img src="icon.armor_t88_u_i00" width=32 height=32></td>
<td align=center><img src="icon.weapon_tallum_blade_i01" width=32 height=32></td>
<td align=center><img src="icon.accessory_ring_of_core_i00" width=32 height=32></td>
</tr>
<tr>
<td align=center><button value="Armors" action="bypass -h npc_%objectId%_Chat 2" {B_BTN}></td>
<td align=center><button value="Weapons" action="bypass -h npc_%objectId%_Chat 1" {B_BTN}></td>
<td align=center><button value="Jewelry" action="bypass -h npc_%objectId%_Chat 3" {B_BTN}></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=center><img src="icon.etc_reagent_white_i00" width=32 height=32></td>
<td align=center><img src="icon.etc_badge_silver_i00" width=32 height=32></td>
<td align=center><img src="icon.etc_royal_membership_i00" width=32 height=32></td>
</tr>
<tr>
<td align=center><button value="Consumables" action="bypass -h npc_%objectId%_Chat 4" {B_BTN}></td>
<td align=center><button value="Event Shop" action="bypass -h npc_%objectId%_Chat 6" {B_BTN}></td>
<td align=center><button value="Donation" action="bypass -h npc_%objectId%_Chat 5" {B_BTN}></td>
</tr>
</table>
<br>
<center><img src="L2UI.SquareGray" width=250 height=1></center>
<button value="Sell Items" action="bypass -h npc_%objectId%_Sell" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009.htm', main_htm)


# --- Weapons HTML ---
weapons_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<font color=3c3c3c>_________</font> <font color=ae9977>Weapons</font> <font color=3c3c3c>_________</font><br>
<br>
<table width=230>
<tr>
<td align=right><img src="icon.weapon_kris_i01" width=32 height=32></td>
<td align=center><button value="B Grade" action="bypass -h npc_%objectId%_multisell 90001" {B_BTN}></td>
<td align=left><img src="icon.weapon_hazard_bow_i01" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.weapon_homunkuluss_sword_i01" width=32 height=32></td>
<td align=center><button value="C Grade" action="bypass -h npc_%objectId%_multisell 90001" {B_BTN}></td>
<td align=left><img src="icon.weapon_eminence_bow_i01" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.weapon_claymore_i01" width=32 height=32></td>
<td align=center><button value="D Grade" action="bypass -h npc_%objectId%_multisell 90001" {B_BTN}></td>
<td align=left><img src="icon.weapon_bichwa_i01" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.weapon_broad_sword_i01" width=32 height=32></td>
<td align=center><button value="No Grade" action="bypass -h npc_%objectId%_multisell 90001" {B_BTN}></td>
<td align=left><img src="icon.weapon_bow_i01" width=32 height=32></td>
</tr>
</table>
<br>
<button value="Back" action="bypass -h npc_%objectId%_Chat 0" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009-1.htm', weapons_htm)


# --- Armors HTML ---
armors_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<font color=3c3c3c>_________</font> <font color=ae9977>Armors Set</font> <font color=3c3c3c>_________</font><br>
<br>
<table width=230>
<tr>
<td align=right><img src="icon.armor_t71_ul_i00" width=32 height=32></td>
<td align=center><button value="B Grade" action="bypass -h npc_%objectId%_multisell 90002" {B_BTN}></td>
<td align=left><img src="icon.armor_t59_ul_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.armor_t21_ul_i00" width=32 height=32></td>
<td align=center><button value="C Grade" action="bypass -h npc_%objectId%_multisell 90002" {B_BTN}></td>
<td align=left><img src="icon.armor_t53_u_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.armor_t05_u_i00" width=32 height=32></td>
<td align=center><button value="D Grade" action="bypass -h npc_%objectId%_multisell 90002" {B_BTN}></td>
<td align=left><img src="icon.armor_t15_ul_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.armor_t01_u_i00" width=32 height=32></td>
<td align=center><button value="No Grade" action="bypass -h npc_%objectId%_multisell 90002" {B_BTN}></td>
<td align=left><img src="icon.armor_leather_shirt_i00" width=32 height=32></td>
</tr>
</table>
<br>
<button value="Back" action="bypass -h npc_%objectId%_Chat 0" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009-2.htm', armors_htm)


# --- Jewels HTML ---
jewels_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<font color=3c3c3c>_________</font> <font color=ae9977>Jewelry</font> <font color=3c3c3c>_________</font><br>
<br>
<table width=230>
<tr>
<td align=right><img src="icon.accessary_ring_of_black_ore_i00" width=32 height=32></td>
<td align=center><button value="B Grade" action="bypass -h npc_%objectId%_multisell 90003" {B_BTN}></td>
<td align=left><img src="icon.accessary_earing_of_black_ore_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.accessary_elven_ring_i00" width=32 height=32></td>
<td align=center><button value="C-D-NG Grade" action="bypass -h npc_%objectId%_multisell 90003" {B_BTN}></td>
<td align=left><img src="icon.accessary_elven_earing_i00" width=32 height=32></td>
</tr>
</table>
<br>
<button value="Back" action="bypass -h npc_%objectId%_Chat 0" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009-3.htm', jewels_htm)


# --- Consumables HTML ---
consumables_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<font color=3c3c3c>_________</font> <font color=ae9977>Consumables</font> <font color=3c3c3c>_________</font><br>
<br>
<table width=230>
<tr>
<td align=right><img src="icon.etc_soul_shot_b_i00" width=32 height=32></td>
<td align=center><button value="Soulshots" action="bypass -h npc_%objectId%_multisell 90004" {B_BTN}></td>
<td align=left><img src="icon.etc_spirit_bullet_blue_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.etc_potion_of_alacrity_i00" width=32 height=32></td>
<td align=center><button value="Potions" action="bypass -h npc_%objectId%_multisell 90004" {B_BTN}></td>
<td align=left><img src="icon.etc_reagent_white_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.etc_scroll_of_escape_i00" width=32 height=32></td>
<td align=center><button value="Scrolls" action="bypass -h npc_%objectId%_multisell 90004" {B_BTN}></td>
<td align=left><img src="icon.etc_scroll_of_resurrection_i00" width=32 height=32></td>
</tr>
</table>
<br>
<button value="Back" action="bypass -h npc_%objectId%_Chat 0" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009-4.htm', consumables_htm)


# --- Donation HTML ---
don_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<font color=3c3c3c>_________</font> <font color=ae9977>Donation Shop</font> <font color=3c3c3c>_________</font><br>
<br>
<table width=230>
<tr>
<td align=right><img src="icon.etc_royal_membership_i00" width=32 height=32></td>
<td align=center><button value="Meraki VIP" action="bypass -h npc_%objectId%_multisell 90005" {B_BTN}></td>
<td align=left><img src="icon.etc_royal_membership_i00" width=32 height=32></td>
</tr>
<tr><td><br></td></tr>
<tr>
<td align=right><img src="icon.accessory_romantic_chapeau_i00" width=32 height=32></td>
<td align=center><button value="Accessories" action="bypass -h npc_%objectId%_multisell 90005" {B_BTN}></td>
<td align=left><img src="icon.accessory_party_hat_i00" width=32 height=32></td>
</tr>
</table>
<br>
<button value="Back" action="bypass -h npc_%objectId%_Chat 0" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009-5.htm', don_htm)


# --- Event HTML ---
evt_htm = f"""<html><title>Meraki Store</title>
<body>
<center>
<font color=3c3c3c>_________</font> <font color=ae9977>Event Shop</font> <font color=3c3c3c>_________</font><br>
<br>
<table width=230>
<tr>
<td align=right><img src="icon.etc_badge_silver_i00" width=32 height=32></td>
<td align=center><button value="Medal Exchange" action="bypass -h npc_%objectId%_multisell 90006" {B_BTN}></td>
<td align=left><img src="icon.etc_badge_silver_i00" width=32 height=32></td>
</tr>
</table>
<br>
<button value="Back" action="bypass -h npc_%objectId%_Chat 0" {B_BTN}>
<font color=3c3c3c>__________________________</font><br>
</center>
</body>
</html>"""
write_file('server_data/game/data/html/merchant/50009-6.htm', evt_htm)

print("Redesign applied successfully using the grid layout.")
