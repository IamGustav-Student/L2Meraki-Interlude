import os
from PIL import Image

# Configuración de rutas
BASE_DIR = r'f:\Programador GS\L2 Meraki'
BRAIN_DIR = r'C:\Users\iamgu\.gemini\antigravity\brain\03687efb-a25b-4a13-a564-cee1ee5e8aab'
ASSETS_OUT = os.path.join(BASE_DIR, 'publish_assets')

# Crear carpeta de salida si no existe
if not os.path.exists(ASSETS_OUT):
    os.makedirs(ASSETS_OUT)

def process_banner():
    # El banner generado es l2_meraki_banner_1777208830540.png
    banner_path = os.path.join(BRAIN_DIR, 'l2_meraki_banner_1777208830540.png')
    if not os.path.exists(banner_path):
        print("Banner no encontrado.")
        return

    img = Image.open(banner_path)
    # Redimensionar para el Community Board (proporción típica)
    img_resized = img.resize((512, 256), Image.Resampling.LANCZOS)
    img_resized = img_resized.convert("RGBA")
    
    out_path = os.path.join(ASSETS_OUT, 'meraki_banner.tga')
    img_resized.save(out_path, format='TGA')
    print(f"Banner procesado y guardado en: {out_path}")

def process_icons():
    # La hoja de iconos es l2_meraki_icons_1777208915190.png
    icons_path = os.path.join(BRAIN_DIR, 'l2_meraki_icons_1777208915190.png')
    if not os.path.exists(icons_path):
        print("Hoja de iconos no encontrada.")
        return

    img = Image.open(icons_path)
    width, height = img.size
    
    # Asumimos una grilla de 4x2 (para 7 iconos) o similar. 
    # El prompt pidió 7 iconos. Vamos a dividirlos manualmente o detectar celdas.
    # Dado que es una imagen generada, intentaremos una división 4x2.
    cell_w = width // 4
    cell_h = height // 2
    
    icon_names = ['home', 'buffer', 'merchant', 'gatekeeper', 'dropsearch', 'delevel', 'premium']
    
    count = 0
    for y in range(2):
        for x in range(4):
            if count >= len(icon_names):
                break
            
            left = x * cell_w
            top = y * cell_h
            right = left + cell_w
            bottom = top + cell_h
            
            icon = img.crop((left, top, right, bottom))
            # Redimensionar a 32x32 (Estándar L2) o 64x64 para mejor calidad
            icon = icon.resize((64, 64), Image.Resampling.LANCZOS)
            icon = icon.convert("RGBA")
            
            name = f"meraki_icon_{icon_names[count]}.tga"
            out_path = os.path.join(ASSETS_OUT, name)
            icon.save(out_path, format='TGA')
            print(f"Icono '{icon_names[count]}' guardado en: {out_path}")
            count += 1

if __name__ == "__main__":
    process_banner()
    process_icons()
    print("\nProceso completado. Todos los assets están listos en 'publish_assets'.")
