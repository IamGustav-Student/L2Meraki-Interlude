import os
import shutil

def sync_assets():
    source_dirs = [
        r'f:\Programador GS\L2 Meraki\tools\CostumeSkins',
        r'f:\Programador GS\L2 Meraki\tools\Crack Shot (Interlude)'
    ]
    
    dest_anim = r'f:\Programador GS\L2 Meraki\client_updates\files\Animations'
    dest_tex = r'f:\Programador GS\L2 Meraki\client_updates\files\Systextures'
    
    os.makedirs(dest_anim, exist_ok=True)
    os.makedirs(dest_tex, exist_ok=True)
    
    extensions = {'.ukx': dest_anim, '.utx': dest_tex}
    
    print("Iniciando sincronizacion de assets...")
    count = 0
    
    # Lista de carpetas encontradas para debug
    found_files = []
    
    for s_dir in source_dirs:
        if not os.path.exists(s_dir):
            print(f"No existe: {s_dir}")
            continue
            
        for root, dirs, files in os.walk(s_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    src_path = os.path.join(root, file)
                    dst_folder = extensions[ext]
                    dst_path = os.path.join(dst_folder, file)
                    
                    # Copiar siempre si no existe
                    if not os.path.exists(dst_path):
                        print(f"Copiando: {file} desde {root}")
                        shutil.copy2(src_path, dst_path)
                        count += 1
                    else:
                        # Si existe, comparar tamaño para estar seguros
                        if os.path.getsize(src_path) != os.path.getsize(dst_path):
                            print(f"Actualizando: {file}")
                            shutil.copy2(src_path, dst_path)
                            count += 1
    
    print(f"Sincronizacion completada. {count} archivos procesados.")

if __name__ == '__main__':
    sync_assets()
