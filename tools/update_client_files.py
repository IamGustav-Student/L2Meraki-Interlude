import os

def read_file(path):
    # Try different encodings
    for enc in ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'cp1252']:
        try:
            with open(path, 'r', encoding=enc) as f:
                content = f.read()
                if content:
                    return content.splitlines(), enc
        except UnicodeDecodeError:
            continue
    raise Exception(f"Could not decode {path}")

def update_itemname():
    path = r'F:\Programador GS\L2 Meraki\tools\itemname-e_final.txt'
    lines, enc = read_file(path)
    print(f"Read itemname ({len(lines)} lines) with {enc}")
    
    # IDs to remove (including the old high IDs and any existing VIP IDs)
    ids_to_remove = {'5249', '6580', '6581', '95000', '95001', '95002', '9500', '9501', '9502'}
    
    new_lines = []
    # Identify header
    header = lines[0]
    
    # Filter rows
    for line in lines[1:]:
        if not line.strip(): continue
        parts = line.split('\t')
        if parts[0].strip() not in ids_to_remove:
            new_lines.append(line)
    
    # Add new VIP lines with SAFER IDs (9500-9502)
    # Using raw strings to avoid escape issues in python
    new_lines.append('9500\tVIP Spirit - 7 Days\t\ta,Enhanced rates and stats for 7 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,')
    new_lines.append('9501\tVIP Spirit - 15 Days\t\ta,Enhanced rates and stats for 15 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,')
    new_lines.append('9502\tVIP Spirit - 30 Days\t\ta,Enhanced rates and stats for 30 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,')
    
    # Write as UTF-8 (no BOM)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines) + '\n')
    print(f"Updated itemname to {len(new_lines)} lines.")

def update_etcitemgrp():
    path = r'F:\Programador GS\L2 Meraki\tools\etcitemgrp_final.txt'
    lines, enc = read_file(path)
    print(f"Read etcitemgrp ({len(lines)} lines) with {enc}")
    
    ids_to_remove = {'95000', '95001', '95002', '9500', '9501', '9502'}
    
    new_lines = []
    for line in lines[1:]:
        if not line.strip(): continue
        parts = line.split('\t')
        if parts[1].strip() not in ids_to_remove:
            new_lines.append(line)
        
    # VIP items use 1\t\t1\t\t for mesh_tex_pair
    line_9500 = '2\t9500\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_talisman_i01\t\t\t\t\t-1\t0\t17\t0\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0'
    line_9501 = '2\t9501\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_talisman_i02\t\t\t\t\t-1\t0\t17\t0\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0'
    line_9502 = '2\t9502\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t00\t\t\ticon.etc_talisman_i03\t\t\t\t\t-1\t0\t17\t0\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t0\t0\t0'
    
    new_lines.append(line_9500)
    new_lines.append(line_9501)
    new_lines.append(line_9502)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines) + '\n')
    print(f"Updated etcitemgrp to {len(new_lines)} lines.")

if __name__ == "__main__":
    update_itemname()
    update_etcitemgrp()
    print("Files patched successfully.")
