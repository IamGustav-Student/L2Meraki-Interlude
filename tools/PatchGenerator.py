import os
import hashlib
import json

# CONFIGURATION
INPUT_DIR = r"f:\Programador GS\L2 Meraki\system_master"
OUTPUT_DIR = r"f:\Programador GS\L2 Meraki\client_updates"
MANIFEST_FILE = "patch.json"

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate_patch():
    print(f"Scanning {INPUT_DIR}...")
    patch_list = []
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    files_out_dir = os.path.join(OUTPUT_DIR, "files")
    
    for root, dirs, files in os.walk(INPUT_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, INPUT_DIR).replace('\\', '/')
            
            # Skip launcher itself or hidden files
            if file == "MerakiLauncher.exe" or file.startswith("."):
                print(f"Skipping excluded file: {file}")
                continue
            
            print(f"Adding to patch: {rel_path}")
                
            md5 = get_md5(full_path)
            size = os.path.getsize(full_path)
            
            print(f"Processing: {rel_path} [{md5}]")
            
            patch_list.append({
                "Path": rel_path,
                "Md5": md5,
                "Size": size
            })
            
            # Copy file to deploy/files structure
            target_path = os.path.join(files_out_dir, rel_path)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(full_path, "rb") as f_in, open(target_path, "wb") as f_out:
                f_out.write(f_in.read())

    # Write manifest
    with open(os.path.join(OUTPUT_DIR, MANIFEST_FILE), "w") as f:
        json.dump(patch_list, f, indent=4)
        
    print("\nDONE!")
    print(f"Upload the contents of '{OUTPUT_DIR}' to your GitHub repository.")

if __name__ == "__main__":
    generate_patch()
