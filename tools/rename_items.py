import os
import re

TOOLS_DIR = r"f:\Programador GS\L2 Meraki\tools"
INPUT_FILE = os.path.join(TOOLS_DIR, "itemname-e.txt")
OUTPUT_FILE = os.path.join(TOOLS_DIR, "itemname-e_ready.txt")

def rename_items():
    if not os.path.exists(INPUT_FILE):
        print(f"No se encontro el archivo: {INPUT_FILE}")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    new_lines = []
    # ID 4358: Bloody Pa'agrio -> Meraki Event
    # ID 6673: Festival Adena -> Meraki Coin
    
    re_paagrio = re.compile(r'^4358\tBloody Pa\'agrio', re.MULTILINE)
    re_adena = re.compile(r'^6673\tFestival Adena', re.MULTILINE)

    count_paagrio = 0
    count_adena = 0

    for line in lines:
        if line.startswith("4358\tBloody Pa'agrio"):
            line = line.replace("Bloody Pa'agrio", "Meraki Event")
            count_paagrio += 1
        elif line.startswith("6673\tFestival Adena"):
            line = line.replace("Festival Adena", "Meraki Coin")
            count_adena += 1
        new_lines.append(line)

    with open(OUTPUT_FILE, 'w', encoding='utf-8', errors='ignore') as f:
        f.write("".join(new_lines))
    
    print(f"Renombrados: Paagrio ({count_paagrio}), Adena ({count_adena})")
    print(f"Archivo guardado en: {OUTPUT_FILE}")

if __name__ == "__main__":
    rename_items()
