import os

# CONFIGURATION
TARGET_DIRS = [
    r"f:\Programador GS\L2 Meraki\system_master",
    r"f:\Programador GS\L2 Meraki\client_updates\files",
    r"f:\Programador GS\L2 Meraki\L2Meraki_Tester_Patch"
]

EXTENSIONS = {'.ukx', '.utx', '.usx', '.u'}

# Valid Headers
# 1. Raw Unreal Package: C1 83 2A 9E
RAW_HEADER = bytes.fromhex("C1 83 2A 9E")
# 2. Lineage 2 Header 111 (Interlude standard)
L2_111_HEADER = b"Lineage2Ver111"

def is_valid_header(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(16)
            if header.startswith(RAW_HEADER):
                return True
            if header.startswith(L2_111_HEADER):
                return True
            return False
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def sanitize():
    print("--- INICIANDO LIMPIEZA DE ASSETS INCOMPATIBLES ---")
    deleted_count = 0
    
    for target_dir in TARGET_DIRS:
        if not os.path.exists(target_dir):
            print(f"Directorio no encontrado: {target_dir}")
            continue
            
        print(f"\nEscaneando: {target_dir}")
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in EXTENSIONS:
                    file_path = os.path.join(root, file)
                    if not is_valid_header(file_path):
                        print(f"[ELIMINADO] Incompatible: {file}")
                        try:
                            os.remove(file_path)
                            deleted_count += 1
                        except Exception as e:
                            print(f"Error eliminando {file}: {e}")
                            
    print(f"\n--- LIMPIEZA COMPLETADA ---")
    print(f"Archivos eliminados: {deleted_count}")

if __name__ == "__main__":
    sanitize()
