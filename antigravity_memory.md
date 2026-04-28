# L2 Meraki - Memoria Persistente de Configuración

> **REGLA DE ORO**: Leer este archivo al iniciar cualquier tarea relacionada con la red, el servidor o el cliente de L2 Meraki.

# Memoria Técnica: Integración de Customs (L2 Meraki)

## Reglas de Oro para Archivos .DAT (Interlude)

1.  **Simetría de Columnas (Armorgrp)**:
    *   Interlude es extremadamente estricto con el conteo de columnas. En este servidor, el `armorgrp.dat` usa **332 columnas** (14 razas con sus respectivos modelos y texturas).
    *   **Error Común**: Pegar líneas de otros packs (Gracia/H5) que tienen más o menos columnas causará el error "Error al guardar" en L2 FileEdit.
    *   **Solución**: Siempre contar las pestañas (`\t`) y compararlas con una línea original funcional.

2.  **Formato de ItemName-e**:
    *   Cada campo de texto debe empezar con el prefijo **`a,`**.
    *   Las descripciones DEBEN terminar con la cadena literal **`\\0`**. Si se usa un byte nulo real (`\0`), el editor o el cliente darán un crash fatal de tipo "Assertion failed".
    *   La estructura estándar de este servidor es de **13 columnas**.

3.  **Codificación y Herramientas**:
    *   Los archivos de texto desencriptados deben guardarse en **UTF-16 LE con BOM**. Sin el BOM, herramientas como `l2asm` o `l2encdec` pueden malinterpretar los datos.
    *   **L2 FileEdit**: Si da error "Cannot open file", usualmente es un error de sintaxis en el TXT o que el archivo `.ddf` no tiene el mismo nombre que el `.txt`.

## Integración Servidor (Mobius Interlude)

1.  **XML de Ítems**:
    *   Usar siempre el atributo `val` (ej: `<set name="is_tradable" val="false" />`) en lugar de `value` para asegurar compatibilidad total con el core Mobius.
    *   El atributo `default_action="EQUIP"` es vital para que el cliente permita usar la skin al hacer doble clic.

2.  **Launcher y Assets**:
    *   Todos los archivos `.ukx` (animaciones) y `.utx` (texturas) deben estar en sus carpetas respectivas en el servidor de actualizaciones.
    *   Es obligatorio regenerar el `patch.json` después de añadir cualquier asset para que el Launcher calcule el hash MD5 y fuerce la descarga.

## Historial de Skins Integradas (Abril 2026)
*   **Crack Shot Pack**: IDs 9910-9914 (Blue, Gold, Pink, Red, Skull).
*   **Costume Pack**: IDs 9930-9936 (JapanGeneral, White Knight, Valkyrie, Cat, Halloween, Ninja, Zaken).
*   **Precios Sugeridos**: 10-15 Donation Coins por set completo.

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
