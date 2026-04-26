import os
import hashlib
import json

# Configuration
WORKSPACE_DIR = r"f:\Programador GS\L2 Meraki"
MASTER_DIR = os.path.join(WORKSPACE_DIR, "system_master")
PATCH_DIR = os.path.join(WORKSPACE_DIR, "client_updates")
PATCH_FILE = os.path.join(PATCH_DIR, "patch.json")
FILES_OUT_DIR = os.path.join(PATCH_DIR, "files")

def get_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate():
    print("Iniciando generación de parche limpio...")
    patch_list = []
    
    if not os.path.exists(MASTER_DIR):
        print(f"Error: Carpeta maestra no encontrada en {MASTER_DIR}")
        return

    # Escanear todo el contenido de system_master de forma recursiva
    print(f"Escaneando {MASTER_DIR}...")
    for root, dirs, files in os.walk(MASTER_DIR):
        for file in files:
            # Evitar archivos ocultos o de sistema
            if file.startswith('.') or '.git' in root:
                continue
                
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, MASTER_DIR)
            
            # No agregar el propio patch.json
            if rel_path == "patch.json":
                continue

            md5 = get_md5(full_path)
            size = os.path.getsize(full_path)
            
            patch_list.append({
                "Path": rel_path,
                "Md5": md5,
                "Size": size
            })
            
            # Sincronizar archivo con la carpeta de parches para el launcher
            target_path = os.path.join(FILES_OUT_DIR, rel_path)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Solo copiar si el archivo es diferente o no existe
            should_copy = True
            if os.path.exists(target_path):
                if get_md5(target_path) == md5:
                    should_copy = False
            
            if should_copy:
                with open(full_path, "rb") as f_in, open(target_path, "wb") as f_out:
                    f_out.write(f_in.read())

    # Guardar manifest
    with open(PATCH_FILE, 'w', encoding='utf-8') as f:
        json.dump(patch_list, f, indent=4)
    
    print(f"Éxito: {len(patch_list)} archivos sincronizados y listos para el Launcher.")

if __name__ == "__main__":
    generate()
