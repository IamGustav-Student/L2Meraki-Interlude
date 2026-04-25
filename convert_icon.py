from PIL import Image

# Open the generated image
img_path = r'C:\Users\iamgu\.gemini\antigravity\brain\55128342-6fee-4c13-a644-61511ba4f216\meraki_vip_icon_1776883609840.png'
img = Image.open(img_path)

# Resize to 32x32 for Lineage 2 icon standard
img = img.resize((32, 32), Image.Resampling.LANCZOS)

# Ensure it's in RGBA (32-bit color with alpha)
img = img.convert("RGBA")

# Save as TGA
out_path = r'f:\Programador GS\L2 Meraki\vip_icon.tga'
img.save(out_path, format='TGA')

print(f"Icon saved successfully to {out_path}")
