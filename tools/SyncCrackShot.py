import os
import shutil
import subprocess

# RUTAS
BASE_DIR = r"f:\Programador GS\L2 Meraki"
SOURCE_ANIM = os.path.join(BASE_DIR, r"tools\Crack Shot (Interlude)\Animations")
TARGET_ANIM = os.path.join(BASE_DIR, r"system_master\Animations")
PATCH_SCRIPT = os.path.join(BASE_DIR, r"tools\PatchGenerator.py")

def sync_assets():
    print("--- INICIANDO SINCRONIZACION DE CRACK SHOT ---")
    
    # 1. Crear carpeta Animations en system_master si no existe
    if not os.path.exists(TARGET_ANIM):
        print(f"Creando directorio: {TARGET_ANIM}")
        os.makedirs(TARGET_ANIM)
    
    # 2. Copiar archivos .ukx
    print("Copiando modelos (.ukx)...")
    for file in os.listdir(SOURCE_ANIM):
        if file.endswith(".ukx"):
            src = os.path.join(SOURCE_ANIM, file)
            dst = os.path.join(TARGET_ANIM, file)
            shutil.copy2(src, dst)
            print(f"  > {file} copiado.")
            
    # 3. Ejecutar el generador de parches
    print("\nEjecutando PatchGenerator.py...")
    try:
        subprocess.run(["python", PATCH_SCRIPT], check=True)
        print("\n--- PROCESO COMPLETADO CON EXITO ---")
        print("Los archivos ya estan en 'client_updates' y el 'patch.json' ha sido actualizado.")
    except Exception as e:
        print(f"Error al ejecutar PatchGenerator: {e}")

if __name__ == "__main__":
    sync_assets()
