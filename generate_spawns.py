import os
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
                            # We found a gatekeeper, generate a spawn for the buffer nearby
                            x = int(npc.get('x')) + 50
                            y = int(npc.get('y')) + 50
                            z = npc.get('z')
                            heading = npc.get('heading')
                            new_spawns.append(f'		<npc id="50008" x="{x}" y="{y}" z="{z}" heading="{heading}" respawnDelay="5" /> <!-- Near GK {npc.get("id")} -->')
            except Exception as e:
                pass # skip parse errors

# Now create the new XML content
xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<list enabled="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../../xsd/spawns.xsd">
	<spawn name="MerakiBuffers_Global">
'''
xml_content += '\n'.join(new_spawns)
xml_content += '''
	</spawn>
</list>
'''

with open('server_data/game/data/spawns/Others/MerakiBuffer.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f"Generated {len(new_spawns)} spawns for Meraki Buffer.")
