import os

def append_if_missing(filepath, id_val, full_line):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if f"\n{id_val}\t" in content or content.startswith(f"{id_val}\t"):
        print(f"ID {id_val} already exists in {filepath}")
    else:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(full_line + '\n')
        print(f"Appended ID {id_val} to {filepath}")

ITEMNAME_MASTER = r'f:\Programador GS\L2 Meraki\tools\itemname_master.txt'

# 1. Adena
append_if_missing(ITEMNAME_MASTER, "57", "57\tAdena\t\ta,Unit of currency in Aden world.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,")
# 2. Wooden Arrow
append_if_missing(ITEMNAME_MASTER, "17", "17\tWooden Arrow\t\ta,An arrow made of wood. It is an arrow used for a no grade bow.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,")
# 3. Meraki VIP - 30 Days (Existing 5249)
append_if_missing(ITEMNAME_MASTER, "5249", "5249\tMeraki VIP - 30 Days\t\ta,Special VIP membership for 30 days.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,")
# 4. Tallum Blade*Dark Legion's Edge
append_if_missing(ITEMNAME_MASTER, "6580", "6580\tTallum Blade*Dark Legion's Edge\t\ta,P.Atk of dual swords will increase more than one-handed type weapon when enchanted. Max HP +15%, Max MP +20%, Max CP +30% when enchanted by 4 or more. Enhances damage to target during PvP.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,")
# 5. Forgotten Blade - Haste
append_if_missing(ITEMNAME_MASTER, "6581", "6581\tForgotten Blade - Haste\t\ta,<Soul Crystal Enhancement>. Increases Atk. Spd. by about 7%. Increases damage inflicted during PvP.\\0\t-1\ta,\ta,\ta,\ta,\t0\t0\t0\ta,")

print("\nAudit fix complete.")
