import os
import subprocess
import re

# CONFIGURACION
TOOLS_DIR = r"f:\Programador GS\L2 Meraki\tools"
SYSTEM_DIR = r"f:\Programador GS\L2 Meraki\system_master\system"
L2ENCDEC = os.path.join(TOOLS_DIR, "l2encdec.exe")

# DATOS PUBLICOS
NEW_IP = "181.2.153.30"
NEW_PORT = "2106"

def run_command(cmd):
    print(f"Ejecutando: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=TOOLS_DIR)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        return False
    return True

def patch_l2ini():
    input_ini = os.path.join(SYSTEM_DIR, "l2.ini")
    dec_ini = os.path.join(SYSTEM_DIR, "l2_dec.ini")
    
    if not os.path.exists(input_ini):
        print(f"No se encontro el archivo: {input_ini}")
        return

    # 1. Desencriptar
    # Comando: l2encdec -d l2.ini l2_dec.ini
    if not run_command([L2ENCDEC, "-d", input_ini, dec_ini]):
        print("Fallo la desencriptacion.")
        return

    # 2. Leer y Modificar
    with open(dec_ini, 'r', encoding='cp1252', errors='ignore') as f:
        content = f.read()

    # Reemplazar IP
    content = re.sub(r'ServerAddr=.*', f'ServerAddr={NEW_IP}', content)
    # Reemplazar Puerto
    content = re.sub(r'Port=.*', f'Port={NEW_PORT}', content)

    with open(dec_ini, 'w', encoding='cp1252') as f:
        f.write(content)
    
    print(f"Archivo modificado con IP: {NEW_IP} y Puerto: {NEW_PORT}")

    # 3. Encriptar de nuevo
    # Comando: l2encdec -e 413 l2_dec.ini l2.ini
    if not run_command([L2ENCDEC, "-e", "413", dec_ini, input_ini]):
        print("Fallo la encriptacion.")
    else:
        print("¡l2.ini actualizado y encriptado correctamente!")
    
    # Limpiar archivo temporal
    if os.path.exists(dec_ini):
        os.remove(dec_ini)

if __name__ == "__main__":
    patch_l2ini()
