import os
import hashlib
import json
import datetime

# CONFIGURATION (Style: Scryde-like robust updater)
UPDATE_DIR = r"F:\Programador GS\L2 Meraki\client_updates"
FILES_DIR = os.path.join(UPDATE_DIR, "files")
MANIFEST_FILE = "patch.json"

# Archivos y extensiones prohibidas en el manifiesto
BLACKLIST_EXT = {'.bak', '.tmp', '.log', '.rar', '.zip', '.crypt', '.copy', '.old'}
BLACKLIST_KEYWORDS = {' copy', 'copia', 'temp_', 'test_'}

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error calculando MD5 para {file_path}: {e}")
        return None

def generate_patch():
    print("="*60)
    print(" L2 MERAKI - REGENERADOR DE MANIFIESTO (MODO ROBUSTO) ")
    print("="*60)
    print(f"Escaneando directorio: {FILES_DIR}")
    
    patch_list = []
    skipped_count = 0
    processed_count = 0
    
    for root, dirs, files in os.walk(FILES_DIR):
        for file in files:
            # 1. Validaciones de Seguridad y Limpieza
            full_path = os.path.join(root, file)
            file_lower = file.lower()
            ext = os.path.splitext(file_lower)[1]
            
            # Omitir archivos ocultos
            if file.startswith("."):
                skipped_count += 1
                continue
                
            # Omitir por extension prohibida
            if ext in BLACKLIST_EXT:
                print(f"[SKIP] Extension no permitida: {file}")
                skipped_count += 1
                continue
            
            # Omitir por palabra clave (como "copy" que causo el error hoy)
            if any(key in file_lower for key in BLACKLIST_KEYWORDS):
                print(f"[WARNING] Archivo sospechoso ignorado: {file}")
                skipped_count += 1
                continue

            # 2. Procesamiento de Ruta
            rel_path = os.path.relpath(full_path, FILES_DIR).replace("\\", "/")
            
            # Validar que la ruta no este vacia o sea puro espacio
            if not rel_path.strip():
                print(f"[ERROR] Ruta vacia detectada para: {file}")
                continue

            # 3. Generacion de Data
            md5 = get_md5(full_path)
            if not md5: continue
            
            size = os.path.getsize(full_path)
            
            patch_list.append({
                "Path": rel_path,
                "Md5": md5,
                "Size": size
            })
            processed_count += 1

    # Estructura final del manifiesto (con metadatos para el launcher)
    # Algunos launchers esperan una lista pura [], otros un objeto {}. 
    # Mantenemos lista [] por compatibilidad con el launcher actual pero limpia.
    
    manifest_path = os.path.join(UPDATE_DIR, MANIFEST_FILE)
    
    try:
        with open(manifest_path, "w") as f:
            json.dump(patch_list, f, indent=4)
        
        print("-" * 60)
        print(f"RESULTADO:")
        print(f" - Archivos procesados: {processed_count}")
        print(f" - Archivos ignorados (Basura/Temp): {skipped_count}")
        print(f" - Manifiesto generado en: {manifest_path}")
        print(f" - Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        
    except Exception as e:
        print(f"ERROR FATAL al escribir el manifiesto: {e}")

if __name__ == "__main__":
    generate_patch()
