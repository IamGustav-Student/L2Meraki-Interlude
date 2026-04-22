# L2 Meraki: Interlude Project Strategy

Estructura de equipo, roles críticos y roadmap para el desarrollo y lanzamiento del servidor Lineage 2 Interlude Meraki.

## Estructura de Equipo (Roles)

### 1. Infraestructura y Backend ("El Arquitecto")
- **Responsabilidades**: Setup de VPS/Dedicado, Docker, optimización de DB (PostgreSQL/MySQL), protección anti-DDoS.
- **Misión**: 99.9% uptime y cero lag.

### 2. Game Design & Data ("El Master")
- **Responsabilidades**: Configuración de `.properties` y DB, rates (XP, SP, Adena, Drop), balanceo de clases (evitar mono-clase), Shop In-Game.
- **Misión**: Economía sustentable no "Pay to Win" extremo.

### 3. Frontend & Web Dev ("El Integrador")
- **Responsabilidades**: Dashboard de usuario, registro, recuperación de password, pasarela de Mercado Pago.
- **Misión**: Flujo impecable desde registro hasta donación.

### 4. Marketing & Growth ("Branding")
- **Responsabilidades**: Contenido para TikTok/Reels, streams en Kick, captación de streamers.
- **Misión**: Llenar el servidor el Día 1.

### 5. Soporte & Comunidad (Head GM)
- **Responsabilidades**: Moderación de Discord, tickets de bugs, control de bots/cheats (SmartGuard).
- **Misión**: Mantener la toxicidad a raya y escuchar al usuario.

---

## Roadmap: L2 Meraki

### Fase 1: Cimientos e Infraestructura (La Base)
- [x] **Entorno de Contenedores**: Setup de Docker (DB, Adminer, Logs).
- [ ] **Selección del Core**: Auditoría del Pack L2J (limpieza y optimización).
- [ ] **Diseño de DB**: Importación de esquemas y optimización de índices.
- [ ] **Seguridad Inicial**: Configuración de firewall y mitigación SQLi.

### Fase 2: Configuración del Game World (El Alma)
- [ ] **Ajuste de Rates**: XP, SP, Adena, Drop, Spoil, Craft.
- [ ] **Economía Base**: Precios en Luxury Shop y NPCs consumibles.
- [ ] **Geodata & Pathnode**: Instalación de archivos de colisiones.
- [ ] **Customización**: Skill "Spirit of Meraki" y sistema VIP.

### Fase 3: Client Side & Branding (La Fachada)
- [ ] **Desarrollo de System**: l2.ini custom, splash screen, anti-edit.
- [ ] **Texturizado**: Iconos (Noblesse Blessing custom) y pantallas de carga.
- [ ] **Web & Registro**: Launcher auto-update y panel de usuario.

### Fase 4: QA & Testing (El Filtro)
- [ ] **Stress Test**: Simular 500+ conexiones.
- [ ] **Pruebas de Balanceo**: Testear skill VIP en diferentes clases.
- [ ] **Closed Alpha**: 5-10 testers de confianza.

### Fase 5: Marketing & Launch (El Grito)
- [ ] **Pre-Lanzamiento**: TikTok/Reels "detrás de escena".
- [ ] **Grand Opening**: Evento en vivo por Kick/YouTube.
- [ ] **Monetización**: Activación de pasarela Mercado Pago.

---

## Buenas Prácticas
- **Versionado (Git)**: Todo cambio en código o XML al repo privado.
- **Backups Automatizados**: Dump de DB cada 6 horas.
- **Documentación**: Planilla de Excel/Notion para IDs de items/skills custom.
