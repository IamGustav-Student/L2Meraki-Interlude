import os
import subprocess
import shutil

# Paths
TOOLS_DIR = r'F:\Programador GS\L2 Meraki\tools'
SYSTEM_MASTER_DIR = r'F:\Programador GS\L2 Meraki\system_master\system'
L2ASM = os.path.join(TOOLS_DIR, 'l2asm.exe')
L2ENCDEC = os.path.join(TOOLS_DIR, 'l2encdec.exe')

def run_cmd(cmd, cwd=TOOLS_DIR):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    return True

def restore_all_dats():
    print("Re-compiling ALL group files from full sources...")
    
    # Files to process: (txt_source, ddf, dat_name, expected_fields)
    tasks = [
        ('itemname_master.txt', 'itemname-e.ddf', 'itemname-e.dat', 13, True), # True means has header
        ('etcitemgrp_master.txt', 'etcitemgrp.ddf', 'etcitemgrp.dat', 32, True),
        ('armorgrp_source.txt', 'armorgrp.ddf', 'armorgrp.dat', 332, False),
        ('weapongrp_source.txt', 'weapongrp.ddf', 'weapongrp.dat', 92, False)
    ]
    
    # First, make sure itemname-e and etcitemgrp have the VIP items
    # We'll update the source files directly
    
    # 1. Update itemname-e_final.txt (base for the process)
    with open(os.path.join(TOOLS_DIR, 'itemname_master.txt'), 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:] # Skip header
    
    ids_to_remove = {'95000', '95001', '95002', '9500', '9501', '9502', '6673'}
    lines = [l for l in lines if l.split('\t')[0].strip() not in ids_to_remove]
    lines.append('6673\tMeraki Coin\t\ta,The official Meraki VIP currency. Tradeable and valuable.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    lines.append('9500\tVIP Meraki - 1 Day\t\ta,Enhanced rates and stats for 1 day.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    lines.append('9501\tVIP Meraki - 15 Days\t\ta,Enhanced rates and stats for 15 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    lines.append('9502\tVIP Meraki - 30 Days\t\ta,Enhanced rates and stats for 30 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    with open(os.path.join(TOOLS_DIR, 'itemname_final_full.txt'), 'w', encoding='utf-8') as f:
        f.writelines(lines)

    # 2. Update etcitemgrp_final.txt
    with open(os.path.join(TOOLS_DIR, 'etcitemgrp_master.txt'), 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:] # Skip header
    lines = [l for l in lines if l.split('\t')[1].strip() not in ids_to_remove]
    # Using icon.etc_scroll_of_return_i01 (Yellow Ticket) for VIP items
    line_9500 = '2\t9500\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_scroll_of_return_i01\t\t\t\t\t-1\t0\t17\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0\n'
    line_9501 = '2\t9501\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_scroll_of_return_i01\t\t\t\t\t-1\t0\t17\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0\n'
    line_9502 = '2\t9502\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_scroll_of_return_i01\t\t\t\t\t-1\t0\t17\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0\n'
    # Meraki Coin (6673) with its original icon
    line_6673 = '2\t6673\t0\t5\t4\t1\t0\tdropitems.drop_coin_of_fair_m00\t\t\tdropitemsTex.drop_coin_of_fair_t00\t\t\ticon.etc_coin_of_fair_i00\t\t\t\t\t0\t0\t8\t0\t0\t1\t\t1\t\t\t\t2\t0\t0\n'
    lines.append(line_9500)
    lines.append(line_9501)
    lines.append(line_9502)
    lines.append(line_6673)
    with open(os.path.join(TOOLS_DIR, 'etcitemgrp_final_full.txt'), 'w', encoding='utf-8') as f:
        f.writelines(lines)

    # Now process everything
    process_file('itemname_final_full.txt', 'itemname-e.ddf', 'itemname-e.dat', 13)
    process_file('etcitemgrp_final_full.txt', 'etcitemgrp.ddf', 'etcitemgrp.dat', 32)
    process_file('armorgrp_source.txt', 'armorgrp.ddf', 'armorgrp.dat', 332)
    process_file('weapongrp_source.txt', 'weapongrp.ddf', 'weapongrp.dat', 92)
    process_file('skillname_master.txt', 'skillname-e.ddf', 'skillname-e.dat', 6)
    process_file('skillgrp_master.txt', 'skillgrp.ddf', 'skillgrp.dat', 17)

def sanitize_line(line, expected_fields):
    parts = line.strip('\n\r').split('\t')
    if len(parts) > expected_fields:
        parts = parts[:expected_fields]
    elif len(parts) < expected_fields:
        parts.extend([''] * (expected_fields - len(parts)))
    return '\t'.join(parts)

def process_file(txt_name, ddf_name, dat_name, expected_fields):
    txt_path = os.path.join(TOOLS_DIR, txt_name)
    temp_txt = os.path.join(TOOLS_DIR, "temp_" + txt_name)
    
    print(f"Processing {txt_name} -> {dat_name}...")
    
    if not os.path.exists(txt_path):
        print(f"  [ERROR] Source {txt_name} not found!")
        return False

    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [sanitize_line(line, expected_fields) for line in f if line.strip()]
        
    with open(temp_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
        
    if run_cmd(f'"{L2ASM}" -d {ddf_name} temp_{txt_name} {dat_name}.dec'):
        if run_cmd(f'"{L2ENCDEC}" -h 413 {dat_name}.dec {dat_name}'):
            shutil.copy2(os.path.join(TOOLS_DIR, dat_name), os.path.join(SYSTEM_MASTER_DIR, dat_name))
            print(f"  [SUCCESS] {dat_name} updated.")
            return True
    print(f"  [FAILED] {dat_name} update failed.")
    return False

if __name__ == "__main__":
    restore_all_dats()
    print("\nSyncing with launcher...")
    run_cmd('python PatchGenerator.py')
    print("\nDONE! All files (Armor, Weapon, Etc, Name) restored and updated.")
