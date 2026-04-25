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

def update_txt_files():
    # Correct itemname-e
    itemname_path = os.path.join(TOOLS_DIR, 'itemname-e_final.txt')
    with open(itemname_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    ids_to_remove = {'95000', '95001', '95002', '9500', '9501', '9502'}
    new_lines = [l for l in lines if l.split('\t')[0].strip() not in ids_to_remove]
    
    # Add corrected VIP lines (ItemName) - exactly 13 fields
    # id(1) name(2) add(3) desc(4) popup(5) sets(6,7,8,9) unk(10,11) spec_enc(12,13)
    new_lines.append('9500\tVIP Spirit - 7 Days\t\ta,Enhanced rates and stats for 7 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    new_lines.append('9501\tVIP Spirit - 15 Days\t\ta,Enhanced rates and stats for 15 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    new_lines.append('9502\tVIP Spirit - 30 Days\t\ta,Enhanced rates and stats for 30 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,\n')
    
    with open(itemname_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    # Correct etcitemgrp
    etc_path = os.path.join(TOOLS_DIR, 'etcitemgrp_final.txt')
    with open(etc_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = [l for l in lines if len(l.split('\t')) > 1 and l.split('\t')[1].strip() not in ids_to_remove]
    
    # Corrected VIP lines (EtcItemGrp) - exactly 32 fields
    line_9500 = '2\t9500\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_talisman_i01\t\t\t\t\t-1\t0\t17\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0\n'
    line_9501 = '2\t9501\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_talisman_i02\t\t\t\t\t-1\t0\t17\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0\n'
    line_9502 = '2\t9502\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_talisman_i03\t\t\t\t\t-1\t0\t17\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0\n'
    
    new_lines.append(line_9500)
    new_lines.append(line_9501)
    new_lines.append(line_9502)
    
    with open(etc_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

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
    
    print(f"Processing {txt_name}...")
    
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
    update_txt_files()
    
    # Process main files
    s1 = process_file('itemname-e_final.txt', 'itemname-e.ddf', 'itemname-e.dat', 13)
    s2 = process_file('etcitemgrp_final.txt', 'etcitemgrp.ddf', 'etcitemgrp.dat', 32)
    
    if s1 and s2:
        print("\nSyncing with launcher...")
        run_cmd('python PatchGenerator.py')
        print("\nDONE! Please run the launcher to update the client.")
    else:
        print("\nSome files failed to compile. Check errors above.")
