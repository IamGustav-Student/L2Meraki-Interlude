# L2 Meraki: Task Tracker

## Matriz de Seguimiento (Status Actual)
- [x] Setup Docker & DB (Completado) - *Antigravity*
- [x] Importación de SQL (Completado - 101 tablas) - *Antigravity*
- [x] Configuración de archivos .ini (Completado) - *Antigravity*
- [x] Registro de Server (hexid) (Completado) - *Antigravity*
- [x] Instalación Java 25 (Compilación) + Java 17 (Runtime) - *Antigravity*
- [x] Compilación del proyecto (BUILD SUCCESSFUL) - *Antigravity*
- [x] Login Server arrancado (Puerto 2106) - *Antigravity*
- [x] Game Server arrancado (Server 1: Bartz) - *Antigravity*
- [/] Branding (Iconos/Logo) (En Diseño) - *Cerebro*
- [x] Integración Skill Spirit of Meraki (Diseñado) - *Cerebro*

---

## Guía de Configuración Técnica

### 1. Organización de Archivos
- [x] Contenido de `dist` movido a `server_data`:
    - `f:\Programador GS\L2 Meraki\server_data\game`
    - `f:\Programador GS\L2 Meraki\server_data\login`
    - `f:\Programador GS\L2 Meraki\server_data\db_installer`

### 2. Inyección de DB en Docker
- [x] Contenedores arriba: `docker-compose up -d`
- [x] MariaDB en `localhost:3306` + Adminer en `localhost:8080`
- [x] Importar SQLs de `db_installer\sql\`: (¡101 tablas importadas!)

### 3. Configuración de archivos .ini
- [x] **Login Server** (`login\config\Database.ini`):
    - URL = `jdbc:mysql://localhost/l2meraki_db...`
    - Login = `meraki_admin`
    - Password = `meraki_password`
- [x] **Game Server** (`game\config\Database.ini`):
    - URL = `jdbc:mysql://localhost/l2meraki_db...`
    - Login = `meraki_admin`
    - Password = `meraki_password`

### 4. Registro de Server
- [x] Ejecutar registro de Server (ID 1).
- [x] Configurar `hexid.txt` en `game\config\`.

### 5. Check de Salud (Java)
- [x] JDK 25 instalado para compilación: `C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot`
- [x] JDK 17 instalado como runtime: `C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot`

### 6. Compilación
- [x] Apache Ant 1.10.17 instalado en `tools\apache-ant-1.10.17`
- [x] Compilados 1609 archivos fuente Java
- [x] JARs generados: `LoginServer.jar` (312KB), `GameServer.jar` (3.9MB), `DatabaseInstaller.jar`
- [x] JARs desplegados en `server_data\libs\`

### 7. Arranque de Servidores
- [x] Login Server: escuchando en `0.0.0.0:2106` (clientes) y `127.0.0.1:9014` (game servers)
- [x] Game Server: Server 1 "Bartz", registrado en Login, **16 segundos de carga**, 2000 slots

---

## Rutas Clave del Proyecto
| Componente | Ruta |
|---|---|
| JDK 25 | `C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot` |
| Ant | `f:\Programador GS\L2 Meraki\tools\apache-ant-1.10.17` |
| Login Server | `f:\Programador GS\L2 Meraki\server_data\login` |
| Game Server | `f:\Programador GS\L2 Meraki\server_data\game` |
| Libs (JARs) | `f:\Programador GS\L2 Meraki\server_data\libs` |
| Docker Compose | `f:\Programador GS\L2 Meraki\docker-compose.yml` |

## Comandos para Arrancar
```powershell
# 1. Levantar Docker (DB + Adminer)
docker-compose -f "f:\Programador GS\L2 Meraki\docker-compose.yml" up -d

# 2. Login Server
cd "f:\Programador GS\L2 Meraki\server_data\login"
& "C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot\bin\java.exe" -server -Dfile.encoding=UTF-8 -Dorg.slf4j.simpleLogger.log.com.zaxxer.hikari=warn -XX:+UseZGC -Xms128m -Xmx256m -jar ../libs/LoginServer.jar

# 3. Game Server
cd "f:\Programador GS\L2 Meraki\server_data\game"
& "C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot\bin\java.exe" -server -Dfile.encoding=UTF-8 -Djava.util.logging.manager=org.l2jmobius.log.ServerLogManager -Dorg.slf4j.simpleLogger.log.com.zaxxer.hikari=warn -XX:+UseZGC -Xmx2g -Xms512m -jar ../libs/GameServer.jar
```
