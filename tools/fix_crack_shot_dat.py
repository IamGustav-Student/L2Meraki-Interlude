import os

# Archivo original
file_path = r"f:\Programador GS\L2 Meraki\tools\Crack Shot (Interlude)\DAT.txt"
output_path = r"f:\Programador GS\L2 Meraki\tools\Crack Shot (Interlude)\DAT_FIXED.txt"

# Iconos de reemplazo (estandar de L2)
DEFAULT_ICON_SUIT = "icon.armor_t91_u_i00" # Icono de Draconic (para el traje)
DEFAULT_ICON_MASK = "icon.etc_fairies_pendant_i00" # Icono de accesorio (para la mascara)

def fix_dat():
    with open(file_path, "r") as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        # Reemplazar iconos personalizados por estandar para evitar crash
        new_line = line.replace("LineageCustom_CrackShotBlue_L2Prague.icons.costume_i00", DEFAULT_ICON_SUIT)
        new_line = new_line.replace("LineageCustom_CrackShotGold_L2Prague.icons.costume_i00", DEFAULT_ICON_SUIT)
        new_line = new_line.replace("LineageCustom_CrackShotPink_L2Prague.icons.costume_i00", DEFAULT_ICON_SUIT)
        new_line = new_line.replace("LineageCustom_CrackShotRed_L2Prague.icons.costume_i00", DEFAULT_ICON_SUIT)
        new_line = new_line.replace("LineageCustom_CrackShotSkull_L2Prague.icons.costume_i00", DEFAULT_ICON_SUIT)
        
        # Iconos de cascos/mascaras
        new_line = new_line.replace("LineageCustom_CrackShotBlue_L2Prague.icons.helmet_i00", DEFAULT_ICON_MASK)
        new_line = new_line.replace("LineageCustom_CrackShotGold_L2Prague.icons.helmet_i00", DEFAULT_ICON_MASK)
        new_line = new_line.replace("LineageCustom_CrackShotPink_L2Prague.icons.helmet_i00", DEFAULT_ICON_MASK)
        new_line = new_line.replace("LineageCustom_CrackShotRed_L2Prague.icons.helmet_i00", DEFAULT_ICON_MASK)
        new_line = new_line.replace("LineageCustom_CrackShotSkull_L2Prague.icons.helmet_i00", DEFAULT_ICON_MASK)
        
        fixed_lines.append(new_line)

    with open(output_path, "w") as f:
        f.writelines(fixed_lines)
    
    print(f"Archivo arreglado creado en: {output_path}")

if __name__ == "__main__":
    fix_dat()
