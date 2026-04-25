import glob
import os

for ms_file in glob.glob('server_data/game/data/multisell/9000*.xml'):
    with open(ms_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the broken tag outside
    if '<npcs><npc>50009</npc></npcs>' in content:
        content = content.replace('\t<npcs><npc>50009</npc></npcs>\n', '')
        content = content.replace('<npcs><npc>50009</npc></npcs>\n', '')
    
    # Inject it properly INSIDE the list tag
    if '<npcs>' not in content:
        # Find the end of the <list ... > tag
        list_end = content.find('>', content.find('<list')) + 1
        content = content[:list_end] + '\n\t<npcs><npc>50009</npc></npcs>' + content[list_end:]
        
    with open(ms_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Multisell XMLs fixed!")
