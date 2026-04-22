# ⚔️ L2 Meraki — Lineage 2 Interlude Server

<p align="center">
  <strong>Un servidor de Lineage 2 Interlude diseñado para una experiencia competitiva, sustentable y con identidad propia.</strong>
</p>

---

## 📋 Descripción

**L2 Meraki** es un servidor privado de Lineage 2 basado en la crónica **Interlude** (C6), construido sobre el emulador [L2jMobius](https://www.l2jmobius.org/).

El nombre "Meraki" (del griego *μεράκι*) significa hacer algo con alma, creatividad y amor — lo que define nuestra filosofía de desarrollo.

### 🎯 Filosofía del Servidor
- **Economía sustentable**: Rates balanceados que incentivan el farmeo y el mercado entre jugadores.
- **Anti Pay-to-Win**: Sistema VIP que otorga comodidad, no poder.
- **Competitividad real**: Balanceo de clases, Olympiad activa y eventos PvP regulares.
- **Comunidad primero**: Límites anti-zerg, soporte activo y transparencia total.

---

## ⚙️ Configuración del Servidor

### Rates
| Rate | Valor | Estrategia |
|---|:---:|---|
| **EXP / SP** | x15 | Ritmo de leveo dinámico |
| **Adena** | x8 | Escasez controlada — incentiva el comercio |
| **Drop General** | x10 | Items accesibles pero no regalados |
| **Spoil** | x12 | Incentiva dwarfs y mercado de materiales |
| **Quest Rewards** | x3 | Evita abuso de quests de adena |

### Stack Tecnológico
| Componente | Tecnología |
|---|---|
| Emulador | L2jMobius — Interlude |
| Lenguaje | Java 25 (Temurin) |
| Base de Datos | MariaDB 10.6 (Docker) |
| Build System | Apache Ant 1.10.17 |
| Contenedores | Docker Compose |

---

## 🚀 Guía de Inicio Rápido

### Prerrequisitos
- [JDK 25 (Eclipse Temurin)](https://adoptium.net/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Apache Ant 1.10.17](https://ant.apache.org/)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/IamGustav-Student/L2Meraki-Interlude.git
cd L2Meraki-Interlude
```

### 2. Levantar la Base de Datos
```bash
docker-compose up -d
```
Esto inicia MariaDB en `localhost:3306` y Adminer en `localhost:8080`.

### 3. Compilar el Proyecto
```bash
# En Windows, usando el Ant incluido o instalado:
ant jar
```
Esto genera `LoginServer.jar`, `GameServer.jar` y `DatabaseInstaller.jar` en `dist/libs/`.

### 4. Desplegar los JARs
Copiar los JARs compilados a `server_data/libs/`.

### 5. Importar las Tablas SQL
```bash
# Desde Docker CLI o Adminer (localhost:8080):
# Importar todos los .sql de server_data/db_installer/sql/
```

### 6. Iniciar los Servidores
```powershell
# Terminal 1: Login Server
cd server_data/login
java -server -Xms128m -Xmx256m -jar ../libs/LoginServer.jar

# Terminal 2: Game Server
cd server_data/game
java -server -Xms512m -Xmx2g -jar ../libs/GameServer.jar
```

---

## 📂 Estructura del Proyecto

```
L2Meraki-Interlude/
├── java/                      # Código fuente Java (Login + Game + Commons)
│   └── org/l2jmobius/
│       ├── commons/           # Utilidades compartidas
│       ├── gameserver/        # Motor del Game Server
│       └── loginserver/       # Motor del Login Server
├── server_data/
│   ├── game/                  # Configuración del Game Server
│   │   ├── config/            # Archivos .ini de configuración
│   │   ├── data/              # NPCs, items, skills, spawns (XML)
│   │   └── script/            # Scripts del servidor (quests, handlers)
│   ├── login/                 # Configuración del Login Server
│   │   └── config/            # Database.ini, Interface.ini
│   ├── db_installer/          # Scripts SQL para la base de datos
│   │   └── sql/               # 101 tablas requeridas
│   └── libs/                  # Dependencias (HikariCP, MySQL Connector, SLF4J)
├── docker-compose.yml         # Infraestructura: MariaDB + Adminer
├── build.xml                  # Script de compilación Ant
└── L2 Meraki.pdf              # Documento de diseño del servidor
```

---

## 🛡️ Roadmap

- [x] **Fase 1**: Infraestructura (Docker, DB, Compilación)
- [x] **Fase 2**: Configuración de Rates
- [ ] **Fase 3**: Sistema de Buffs (20+4 slots, 1hr duración)
- [ ] **Fase 4**: Enchant System (Safe +3, Max +16, 66% rate)
- [ ] **Fase 5**: Sistema VIP & Skill "Spirit of Meraki"
- [ ] **Fase 6**: Límites Anti-Zerg y Seguridad (HWID, Dual-box)
- [ ] **Fase 7**: Eventos Automáticos (TvT, CtF, DM)
- [ ] **Fase 8**: Configuración de Cliente
- [ ] **Fase 9**: Landing Page & Dashboard Web
- [ ] **Fase 10**: Integración Mercado Pago (Donaciones)

---

## 📊 Base de Datos

| Parámetro | Valor |
|---|---|
| Motor | MariaDB 10.6 |
| Database | `l2meraki_db` |
| Puerto | `3306` |
| Adminer | `http://localhost:8080` |

---

## 📄 Licencia

Este proyecto es un servidor privado de Lineage 2 con fines educativos y de entretenimiento.
El código del emulador está basado en [L2jMobius](https://www.l2jmobius.org/) bajo sus respectivos términos.

---

<p align="center">
  <em>Hecho con μεράκι (Meraki) — con alma y creatividad.</em>
</p>
