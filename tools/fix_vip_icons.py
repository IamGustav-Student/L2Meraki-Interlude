import os

def replace_in_file(filepath, search_pattern, replacement_line):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    found = False
    for line in lines:
        if search_pattern in line:
            new_lines.append(replacement_line + '\n')
            found = True
        else:
            new_lines.append(line)
    
    if not found:
        print(f"Pattern {search_pattern} not found in {filepath}, appending instead.")
        new_lines.append(replacement_line + '\n')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated {filepath}")

# Update with guaranteed working icon: icon.etc_coins_gold_i00
# 9500
replace_in_file(r'f:\Programador GS\L2 Meraki\tools\etcitemgrp_master.txt', 
                "\t9500\t", 
                "2\t9500\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t01\t\t\ticon.etc_coins_gold_i00\t\t\t\t\t-1\t10\t0\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t2\t0\t0")
# 9501
replace_in_file(r'f:\Programador GS\L2 Meraki\tools\etcitemgrp_master.txt', 
                "\t9501\t", 
                "2\t9501\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t01\t\t\ticon.etc_coins_gold_i00\t\t\t\t\t-1\t10\t0\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t2\t0\t0")
# 9502
replace_in_file(r'f:\Programador GS\L2 Meraki\tools\etcitemgrp_master.txt', 
                "\t9502\t", 
                "2\t9502\t0\t3\t2\t5\t0\tdropitems.drop_sack_m00\t\t\tdropitemstex.drop_sack_t01\t\t\ticon.etc_coins_gold_i00\t\t\t\t\t-1\t10\t0\t0\t0\t1\t\t1\t\tItemSound.itemdrop_sack\t\t2\t0\t0")
