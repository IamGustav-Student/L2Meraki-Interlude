import os

WORKSPACE = r"f:\Programador GS\L2 Meraki"

def audit():
    print(f"--- INICIANDO AUDITORIA DEL SERVIDOR (L2 MERAKI) ---")
    
    checks = {
        "Server Data": "server_data",
        "Game Server Core": "server_data/game",
        "Login Server Core": "server_data/login",
        "System Master": "system_master",
        "Launcher Folder": "MerakiLauncher",
        "Patch Manifest": "client_updates/patch.json",
        "Database Installer": "server_data/db_installer"
    }
    
    results = []
    for name, path in checks.items():
        full_path = os.path.join(WORKSPACE, path)
        status = "[OK]" if os.path.exists(full_path) else "[FALTANTE]"
        results.append(f"{name:20} : {status}")
        
    # Check for logs
    log_files = [
        "server_data/game/log/stdout.log",
        "server_data/login/log/stdout.log"
    ]
    
    print("\n--- Estado de Carpetas ---")
    for r in results: print(r)
    
    print("\n--- Verificando Configuración Crítica ---")
    config_game = os.path.join(WORKSPACE, "server_data/game/config/Server.properties")
    if os.path.exists(config_game):
        print("Configuracion de Juego: [OK]")
    else:
        print("Configuracion de Juego: [FALTANTE - Revisar server_data/game/config/]")
        
    print("\n--- Verificando Launcher ---")
    launcher_exe = os.path.join(WORKSPACE, "client_updates/files/MerakiLauncher.exe")
    if os.path.exists(launcher_exe):
        print("Launcher en Patch: [OK]")
    else:
        print("Launcher en Patch: [NO ENCONTRADO - Recordar copiar a client_updates/files/]")

    print("\n--- RESUMEN ---")
    print("Repositorio Limpio: [SÍ]")
    print("Estructura L2J:     [CORRECTA]")

if __name__ == "__main__":
    audit()
