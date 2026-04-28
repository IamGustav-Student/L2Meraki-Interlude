# L2 Meraki - Memoria Persistente de Configuración

> **REGLA DE ORO**: Leer este archivo al iniciar cualquier tarea relacionada con la red, el servidor o el cliente de L2 Meraki.

## 🌐 Configuración de Red Actual
- **IP Pública**: `181.2.153.30` (IP Dinámica - Verificar si falla la conexión).
- **Puerto Login (Público)**: `2106`
- **Puerto Game (Público)**: `7777`
- **Método de Conexión**: Port Forwarding (Router Sagemcom).
- **IP Local del Servidor**: `192.168.1.3`

## 🚀 Launcher y Cliente
- **URL de Actualizaciones**: `https://raw.githubusercontent.com/IamGustav-Student/L2Meraki-Interlude/main/client_updates/`
- **Archivo l2.ini (Público)**: Configurado con la IP `181.2.153.30` y puerto `2106`.
- **Acceso Local (Dev)**: Usar carpeta `system_local` o manual con IP `127.0.0.1`.
- **Encriptación**: Header 413 (Blowfish). Usar `tools\l2encdec.exe`.

## 🛠 Herramientas de Automatización
1. **Patch l2.ini**: `python tools\auto_patch_l2ini.py` (Actualiza IP en el cliente maestro).
2. **Generar Parche**: `python tools\PatchGenerator.py` (Sincroniza archivos para el Launcher).
3. **UPnP Tool**: `python tools\upnp_tool.py` (Intenta abrir puertos automáticamente).

## 🗺️ Hoja de Ruta de Desarrollo (Basado en PDF)

### 1. Configuración de Base (Rates)
- **General**: Exp x15, SP x15, Adena x8, Drop x10, Spoil x12, Quest x3.
- **Economía**: Grado D/C en Giran. Grado B/A/S únicamente por craft.

### 2. Sistema de Buffs & VIP
- **Buffs NPC**: 1ra/2da clase (1h) Gratis. Danzas/Songs (1h) Costo elevado.
- **No en NPC**: Buffs de 3ra clase (Resists, PoV, CoV).
- **VIP (Meraki Blessing)**: x20 Exp/SP, x10 Adena, 3 ventanas, 2h buffs, +10% PvE Stats, Cuadro Dorado.

### 3. Mecánicas de Juego (Mecánicas Técnicas)
- **Límites**: 2 ventanas por HWID (3 VIP).
- **Subclase/Nobleza**: Quest simplificada. Alternativa de compra con Event Medals + Adena (Shop Universal).
- **Enchant**: Safe +3 (Pecheras +4), Máximo +16. Rate 66%.
- **Lucky Scroll**: Protección total (no rompe, no baja nivel). Costo: 50 Medals + 5M Adena.

### 4. End-Game & Competencia (Anti-Zerg)
- **Clanes**: Máximo 45 miembros (5 partys). Alianzas: Máximo 2 clanes.
- **Bosses Épicos**: Horarios fijos con anuncio global 15 min antes.
- **Olimpíadas**: Período de 15 días. Restricción de Enchant a +6 (automático).
- **Asedios**: Fines de semana 20:00 hs (Arg). Shop especial por Tiers de castillos.

### 5. Pendientes Técnicos Vitales
- [ ] Implementar comando `.offline` shop.
- [ ] Configurar protección Anti-Bot (Strix o similar).
- [ ] Cargar Geodata Premium para evitar que mobs atraviesen paredes.
- [ ] Configurar comandos `.menu`, `.repair` y `.stats`.

## 📜 Bitácora de Configuraciones Aplicadas
- **[27/04/2026]**: 
    - ✅ **Spoil**: Ajustado a x12 en `Rates.ini`.
    - ✅ **Alianzas**: Limitadas a 2 clanes en `Player.ini` (Anti-Zerg).
    - ✅ **VIP (Exp/SP)**: Ajustado a x20 exactos (Factor 1.3333) en `PremiumSystem.ini`.
    - ✅ **VIP (Adena)**: Ajustado a x10 exactos (Factor 1.25) en `PremiumSystem.ini`.
    - ✅ **Community Board**: Rediseñada la página principal (`homepage.html`) con el estilo Meraki Dashboard y lista de comandos.
    - ✅ **Comandos**: Verificados y listados `.menu`, `.repair`, `.stats`, `.premium`, `.offline` y `.apon/.apoff`.
    - ✅ **Peso (Weight Limit)**:
        - Base: +20% para todos los jugadores (`AltWeightLimit = 1.2`).
        - VIP: +50% adicional mediante la habilidad pasiva `Spirit of Meraki` (Skill ID 9000).
    - ✅ **Automatización VIP**: Implementado `PremiumSkillHandler.java` para otorgar/quitar automáticamente la Skill 9000 según el estado Premium del jugador al loguear.
    - ✅ **Skins Crack Shot**: 
        - Integradas 5 variaciones de trajes (IDs 9910-9914) y máscaras (9810-9814).
        - Automatizado el despliegue mediante `SyncCrackShot.py`.
        - Manifiesto `patch.json` actualizado para descarga automática vía Launcher.
