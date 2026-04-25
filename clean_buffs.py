import xml.etree.ElementTree as ET

tree = ET.parse('server_data/game/data/SchemeBufferSkills.xml')
root = tree.getroot()

to_remove = {'1355', '1356', '1357', '1363', '1413', '4702', '4703', '4700', '4699', '1352', '1353', '1354'}
kept_ids = set()

for category in root.findall('category'):
    if category.get('type') == 'Special':
        root.remove(category)
        continue
    
    for buff in category.findall('buff'):
        if buff.get('id') in to_remove:
            category.remove(buff)
        else:
            kept_ids.add(buff.get('id'))

# Format for SkillDurationList
duration_list = ';'.join(f"{bid},3600" for bid in sorted(kept_ids, key=int)) + ';'

# Save cleaned XML
tree.write('server_data/game/data/SchemeBufferSkills.xml', encoding='UTF-8', xml_declaration=True)
print("SkillDurationList = " + duration_list)
