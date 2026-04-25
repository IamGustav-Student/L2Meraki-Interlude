import os

html_dir = r"f:\Programador GS\L2 Meraki\server_data\game\data\html\teleporter"
global_menu_content = """<html>
<title>Gatekeeper - Meraki</title>

<body>
	<center>
		<img src="L2UI_CH3.onscrmsg_pattern01_1" width=300 height=32>
		<br>
		<font color="LEVEL">Meraki Global Gatekeeper</font>
		<br>
		<table width=270>
			<tr>
				<td align=center>
					<table width=250 bgcolor=000000>
						<tr>
							<td align=right width=40><img src="icon.etc_adventure_map_i00" width=32 height=32></td>
							<td align=center width=150>
								<font color="LEVEL">Teleport Global</font>
								<br1>Selecciona tu destino
							</td>
							<td align=left width=40><img src="icon.etc_adventure_map_i00" width=32 height=32></td>
						</tr>
					</table>
				</td>
			</tr>
		</table>
		<br>
		<table width=240>
			<tr>
				<td align=right><img src="icon.etc_castle_i00" width=32 height=32></td>
				<td align=center><button value="Towns" action="bypass -h npc_%objectId%_Chat 10" width=85 height=21
						back="L2UI_ch3.Btn1_normalOn" fore="L2UI_ch3.Btn1_normalOn"></td>
				<td align=left><img src="icon.etc_castle_i00" width=32 height=32></td>
			</tr>
			<tr>
				<td align=right><img src="icon.etc_old_map_i00" width=32 height=32></td>
				<td align=center><button value="Farm Zones" action="bypass -h npc_%objectId%_Chat 11" width=85 height=21
						back="L2UI_ch3.Btn1_normalOn" fore="L2UI_ch3.Btn1_normalOn"></td>
				<td align=left><img src="icon.etc_old_map_i00" width=32 height=32></td>
			</tr>
			<tr>
				<td align=right><img src="icon.etc_desert_i00" width=32 height=32></td>
				<td align=center><button value="Leveling" action="bypass -h npc_%objectId%_Chat 12" width=85 height=21
						back="L2UI_ch3.Btn1_normalOn" fore="L2UI_ch3.Btn1_normalOn"></td>
				<td align=left><img src="icon.etc_desert_i00" width=32 height=32></td>
			</tr>
			<tr>
				<td align=right><img src="icon.skill4045" width=32 height=32></td>
				<td align=center><button value="Noblesse" action="bypass -h npc_%objectId%_showNoblesSelect" width=85 height=21
						back="L2UI_ch3.Btn1_normalOn" fore="L2UI_ch3.Btn1_normalOn"></td>
				<td align=left><img src="icon.skill4045" width=32 height=32></td>
			</tr>
			<tr>
				<td align=right><img src="icon.etc_whiteday_herb_i00" width=32 height=32></td>
				<td align=center><button value="Arenas" action="bypass -h npc_%objectId%_showTeleports list3" width=85
						height=21 back="L2UI_ch3.Btn1_normalOn" fore="L2UI_ch3.Btn1_normalOn"></td>
				<td align=left><img src="icon.etc_whiteday_herb_i00" width=32 height=32></td>
			</tr>
		</table>
		<br>
		<img src="L2UI_CH3.onscrmsg_pattern01_1" width=300 height=32>
	</center>
</body>

</html>"""

# Submenus need to be copied too for each NPC
submenus = {
    "10": "50009-10.htm",
    "11": "50009-11.htm",
    "12": "50009-12.htm"
}

target_npcs = [
    "30006", "30059", "30080", "30134", "30146", "30177", "30233", "30256", "30320", 
    "30540", "30576", "30716", "30719", "30722", "30727", "30836", "30848", "30878", 
    "30899", "31275", "31320", "31698", "31699", "31964"
]

for npc_id in target_npcs:
    # Main menu
    main_file = os.path.join(html_dir, f"{npc_id}.htm")
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(global_menu_content)
    
    # Submenus
    for suffix, source_name in submenus.items():
        source_path = os.path.join(html_dir, source_name)
        with open(source_path, "r", encoding="utf-8") as sf:
            submenu_content = sf.read()
        
        target_path = os.path.join(html_dir, f"{npc_id}-{suffix}.htm")
        with open(target_path, "w", encoding="utf-8") as tf:
            tf.write(submenu_content)

print(f"Updated {len(target_npcs)} NPCs with global menu and submenus.")
