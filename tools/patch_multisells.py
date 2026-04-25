import os

MULTISELL_DIRS = [
    r'f:\Programador GS\L2 Meraki\server_data\game\data\multisell',
    r'f:\Programador GS\L2 Meraki\server_data\game\data\multisell\custom'
]

def patch_multisell(dir_path, filename):
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<npcs>' in content:
        if '<npc>-1</npc>' in content:
            # print(f"Skipping {filename}: Already patched.")
            return
        else:
            new_content = content.replace('<npcs>', '<npcs>\n\t\t<npc>-1</npc>')
    else:
        new_content = content.replace('</list>', '\t<npcs>\n\t\t<npc>-1</npc>\n\t</npcs>\n</list>')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched {filename} in {dir_path}")

for d in MULTISELL_DIRS:
    if os.path.exists(d):
        for file in os.listdir(d):
            if file.endswith('.xml'):
                patch_multisell(d, file)

print("\nFull Multisell allowance patch complete.")
