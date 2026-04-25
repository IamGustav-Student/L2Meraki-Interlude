import os

def patch_file(filename, lines_to_add):
    # Read first to check if already patched (though we re-disassembled, so it's fresh)
    with open(filename, 'a', encoding='utf-8') as f:
        for line in lines_to_add:
            f.write(line + '\n')
    print(f"Patched {filename}")

# ItemName-e lines (IDs 5249, 6580, 6581)
itemname_lines = [
    "5249\tMeraki VIP (30 Days)\t\ta,Increases EXP/SP, Drop, Spoil and Adena rates by x2.0 for 30 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,",
    "6580\tMeraki VIP (1 Day)\t\ta,Increases EXP/SP, Drop, Spoil and Adena rates by x1.2 for 24 hours.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,",
    "6581\tMeraki VIP (15 Days)\t\ta,Increases EXP/SP, Drop, Spoil and Adena rates by x1.5 for 15 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,"
]

# EtcItemGrp lines (matching new header)
# Note: durability -1, weight 0, material 3 (cloth/etc), crystallizable 0, type1 0
# mesh_tex_pair_cntm 0, mesh_tex_pair_cntt 0
# etcitemgrp header has 32 fields.
# 2(tag) 5249(id) 0 3 6 3 0 (drop) none none none (mesh) none none none (tex) icon.etc_royal_membership_i00 none none none none -1 0 3 0 0 0(cntm) 0(cntt) ItemSound.itemdrop_scroll none 1 0 0
etcitemgrp_lines = [
    "2\t5249\t0\t3\t6\t3\t0\tdropitems.drop_scroll_m00\t\t\tdropitemstex.drop_scroll_t00\t\t\ticon.etc_royal_membership_i00\t\t\t\t\t-1\t0\t3\t0\t0\t0\t\t0\t\tItemSound.itemdrop_scroll\t\t1\t0\t0",
    "2\t6580\t0\t3\t6\t3\t0\tdropitems.drop_scroll_m00\t\t\tdropitemstex.drop_scroll_t00\t\t\ticon.etc_royal_membership_i00\t\t\t\t\t-1\t0\t3\t0\t0\t0\t\t0\t\tItemSound.itemdrop_scroll\t\t1\t0\t0",
    "2\t6581\t0\t3\t6\t3\t0\tdropitems.drop_scroll_m00\t\t\tdropitemstex.drop_scroll_t00\t\t\ticon.etc_royal_membership_i00\t\t\t\t\t-1\t0\t3\t0\t0\t0\t\t0\t\tItemSound.itemdrop_scroll\t\t1\t0\t0"
]

patch_file("itemname-e_final.txt", itemname_lines)
patch_file("etcitemgrp_final.txt", etcitemgrp_lines)
