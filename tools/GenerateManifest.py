import os
import hashlib
import json

# CONFIGURATION
UPDATE_DIR = r"F:\Programador GS\L2 Meraki\client_updates"
FILES_DIR = os.path.join(UPDATE_DIR, "files")
MANIFEST_FILE = "patch.json"

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate_patch():
    print(f"Scanning {FILES_DIR}...")
    patch_list = []
    
    for root, dirs, files in os.walk(FILES_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            # Relative path from FILES_DIR (e.g. system/itemname-e.dat)
            rel_path = os.path.relpath(full_path, FILES_DIR)
            
            # Skip hidden files
            if file.startswith("."):
                continue
                
            md5 = get_md5(full_path)
            size = os.path.getsize(full_path)
            
            print(f"Processing: {rel_path} [{md5}]")
            
            patch_list.append({
                "Path": rel_path.replace("\\", "/"),
                "Md5": md5,
                "Size": size
            })

    # Write manifest
    manifest_path = os.path.join(UPDATE_DIR, MANIFEST_FILE)
    with open(manifest_path, "w") as f:
        json.dump(patch_list, f, indent=4)
        
    print(f"\nDONE! Manifest generated at {manifest_path}")

if __name__ == "__main__":
    generate_patch()
