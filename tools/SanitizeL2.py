import os

def sanitize_file(file_path, output_path):
    print(f"Sanitizando {file_path}...")
    try:
        # Leer como latin-1 para preservar los bytes originales de L2
        with open(file_path, 'r', encoding='latin-1') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error leyendo archivo: {e}")
        return

    sanitized_lines = []
    # Saltamos la cabecera
    for line in lines[1:]:
        # Reemplazamos el caracter corrupto (Caf) por e normal
        # Buscamos el byte problematico \xef\xbf\xbd o similar que se ve como  en el editor
        clean_line = line.encode('utf-8', 'ignore').decode('utf-8')
        sanitized_lines.append(clean_line)

    # Escribimos en UTF-8 puro (sin BOM) para l2asm
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(sanitized_lines)
    print(f"Archivo guardado en {output_path}")

if __name__ == '__main__':
    sanitize_file(r'f:\Programador GS\L2 Meraki\tools\itemname-e.txt', r'f:\Programador GS\L2 Meraki\tools\itemname_clean.txt')
    sanitize_file(r'f:\Programador GS\L2 Meraki\tools\armorgrp.txt', r'f:\Programador GS\L2 Meraki\tools\armorgrp_clean.txt')
