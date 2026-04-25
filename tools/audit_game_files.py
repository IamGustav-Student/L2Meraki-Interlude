import os
import xml.etree.ElementTree as ET
import re

# Paths
SERVER_SKILLS_DIR = r'f:\Programador GS\L2 Meraki\server_data\game\data\stats\skills'
SERVER_ITEMS_DIR = r'f:\Programador GS\L2 Meraki\server_data\game\data\stats\items'
TOOLS_DIR = r'f:\Programador GS\L2 Meraki\tools'

CLIENT_SKILLNAME = os.path.join(TOOLS_DIR, 'skillname_master.txt')
CLIENT_SKILLGRP = os.path.join(TOOLS_DIR, 'skillgrp_master.txt')
CLIENT_ITEMNAME = os.path.join(TOOLS_DIR, 'itemname_master.txt')
CLIENT_ETCGRP = os.path.join(TOOLS_DIR, 'etcitemgrp_master.txt')
CLIENT_ARMORGRP = os.path.join(TOOLS_DIR, 'armorgrp_source.txt')
CLIENT_WEAPONGRP = os.path.join(TOOLS_DIR, 'weapongrp_source.txt')

def get_server_skill_ids():
    skill_ids = set()
    for filename in os.listdir(SERVER_SKILLS_DIR):
        if filename.endswith('.xml'):
            try:
                tree = ET.parse(os.path.join(SERVER_SKILLS_DIR, filename))
                root = tree.getroot()
                for skill in root.findall('skill'):
                    skill_id = skill.get('id')
                    if skill_id:
                        skill_ids.add(int(skill_id))
            except Exception as e:
                print(f"Error parsing skill file {filename}: {e}")
    return skill_ids

def get_server_item_ids():
    item_ids = set()
    for filename in os.listdir(SERVER_ITEMS_DIR):
        if filename.endswith('.xml'):
            try:
                tree = ET.parse(os.path.join(SERVER_ITEMS_DIR, filename))
                root = tree.getroot()
                for item in root.findall('item'):
                    item_id = item.get('id')
                    if item_id:
                        item_ids.add(int(item_id))
            except Exception as e:
                print(f"Error parsing item file {filename}: {e}")
    return item_ids

def get_client_ids(filepath, id_column=0, has_header=True):
    ids = set()
    if not os.path.exists(filepath):
        print(f"Warning: Client file {filepath} not found.")
        return ids
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        if has_header:
            lines = lines[1:]
        for line in lines:
            parts = line.split('\t')
            if len(parts) > id_column:
                try:
                    val = parts[id_column].strip()
                    if val.isdigit():
                        ids.add(int(val))
                except:
                    pass
    return ids

def audit():
    print("--- LINEAGE 2 MERAKI AUDIT ---")
    
    # 1. Skills Audit
    print("\n[SKILLS AUDIT]")
    server_skills = get_server_skill_ids()
    client_skillnames = get_client_ids(CLIENT_SKILLNAME, 0, True)
    client_skillgrps = get_client_ids(CLIENT_SKILLGRP, 0, True)
    
    missing_skillname = server_skills - client_skillnames
    missing_skillgrp = server_skills - client_skillgrps
    
    print(f"Total Server Skills: {len(server_skills)}")
    print(f"Skills missing in skillname-e: {len(missing_skillname)}")
    print(f"Skills missing in skillgrp: {len(missing_skillgrp)}")
    
    if missing_skillname:
        print(f"Sample missing names: {list(missing_skillname)[:10]}")
    if missing_skillgrp:
        print(f"Sample missing grps: {list(missing_skillgrp)[:10]}")

    # 2. Items Audit
    print("\n[ITEMS AUDIT]")
    server_items = get_server_item_ids()
    client_itemnames = get_client_ids(CLIENT_ITEMNAME, 0, True)
    
    # Client items are split across etc, armor, weapon
    client_etc = get_client_ids(CLIENT_ETCGRP, 1, True) # etcitemgrp id is in column 1
    client_armor = get_client_ids(CLIENT_ARMORGRP, 1, False) # armorgrp id in col 1, no header
    client_weapon = get_client_ids(CLIENT_WEAPONGRP, 1, False) # weapongrp id in col 1, no header
    
    client_itemgrps = client_etc | client_armor | client_weapon
    
    missing_itemname = server_items - client_itemnames
    missing_itemgrp = server_items - client_itemgrps
    
    print(f"Total Server Items: {len(server_items)}")
    print(f"Items missing in itemname-e: {len(missing_itemname)}")
    print(f"Items missing in grp files (etc/armor/weapon): {len(missing_itemgrp)}")
    
    if missing_itemname:
        print(f"Sample missing names: {list(missing_itemname)[:10]}")
    if missing_itemgrp:
        print(f"Sample missing grps: {list(missing_itemgrp)[:10]}")
        
    # Check for Interlude base ranges
    # Standard skills go up to 4000 (roughly)
    # Items go up to 10000 (roughly)
    
    # Save results to a file
    with open('audit_results.txt', 'w') as f:
        f.write(f"Missing Skillnames: {sorted(list(missing_skillname))}\n")
        f.write(f"Missing Skillgrps: {sorted(list(missing_skillgrp))}\n")
        f.write(f"Missing Itemnames: {sorted(list(missing_itemname))}\n")
        f.write(f"Missing Itemgrps: {sorted(list(missing_itemgrp))}\n")

if __name__ == "__main__":
    audit()
