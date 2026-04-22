# L2 Meraki: Guía de Niveles de Acceso y Roles GM

> Fuente: [AccessLevels.xml](file:///f:/Programador%20GS/L2%20Meraki/server_data/game/config/AccessLevels.xml) + [AdminCommands.xml](file:///f:/Programador%20GS/L2%20Meraki/server_data/game/config/AdminCommands.xml)

## Tabla de Roles

| Nivel | Rol | isGM | Color Nombre | Permisos Clave |
|:---:|---|:---:|---|---|
| **-1** | Banned | ❌ | Blanco | Sin daño, sin trade, sin exp. Baneado total. |
| **0** | User | ❌ | Blanco | Jugador normal. Trade, daño, exp. |
| **10** | Chat Moderator | ❌ | Blanco | = User pero puede moderar chat |
| **20** | Test GM | ❌ | Blanco | Alt+G ✅, Res fija, sin trade, sin daño, sin exp |
| **30** | General GM | ❌ | Azul | Alt+G ✅, hereda de Test GM |
| **40** | Support GM | ❌ | Verde oscuro | Hereda de General GM |
| **50** | Event GM | ❌ | Verde | Hereda de Support GM |
| **60** | Head GM | ❌ | Rojo oscuro | Trade ✅, Daño ✅, Exp ✅, hereda todo |
| **70** | Admin | ✅ | Verde brillante | **Primer nivel con isGM=true**. Todo habilitado. |
| **100** | Master | ✅ | Celeste | **Máximo nivel**. Acceso total a todos los comandos. |

> [!IMPORTANT]
> Solo los niveles **70 (Admin)** y **100 (Master)** tienen `isGM = true`. Los niveles 10-60 pueden usar Alt+G y ciertos comandos pero **NO son reconocidos como GM por el sistema**.

## Permisos por Nivel

| Permiso | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 100 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| isGM | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Peace Attack | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Fixed Res | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Trade | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Alt+G | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Give Damage | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Take Aggro | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Gain Exp | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |

## Comandos por Nivel Mínimo

### Nivel 30 (General GM) — 56 comandos
Comandos básicos de gestión y navegación:
- `//admin` — Abrir menú principal GM
- `//invis` / `//invisible` — Hacerse invisible
- `//invul` — Invulnerabilidad
- `//gmspeed 1-10` — Velocidad GM
- `//goto` — Teleportarse a ubicación/jugador
- `//teleportto` — TP a jugador por nombre
- `//announce` — Anuncios al server
- `//ban_acc` / `//ban_char` — Banear
- `//server_shutdown` / `//server_restart` — Apagar/Reiniciar server
- `//find_character` / `//find_ip` — Buscar jugadores
- `//scan` / `//search` — Buscar NPCs/Items
- `//serverinfo` — Info del servidor

### Nivel 100 (Master) — 440+ comandos
Todo lo anterior más los comandos críticos:
- `//set_level 80` — Setear nivel
- `//give_all_skills` — Dar todas las skills
- `//create_item ID CANTIDAD` — Crear items
- `//enchant` — Enchantear equipamiento
- `//setclass` — Cambiar clase
- `//setnoble` — Dar nobleza
- `//sethero` — Dar hero
- `//changelvl` — Cambiar access level de otro jugador
- `//kill` / `//res` — Matar/Revivir
- `//kick` — Expulsar jugador
- `//heal` — Full HP/MP/CP
- `//spawn` — Spawnear NPCs/Mobs
- `//siege` — Control de asedios
- `//grandboss` — Control de Grand Bosses
- `//reload` — Recargar configs del server
- `//premium_add1/2/3` — Dar premium

## Comando para Cambiar Access Level en DB

```sql
-- Dar Master (nivel máximo) a una cuenta y personaje
UPDATE accounts SET accessLevel = 100 WHERE login = 'nombre_cuenta';
UPDATE characters SET accesslevel = 100 WHERE account_name = 'nombre_cuenta';
```

> [!WARNING]
> El cambio requiere **relog del personaje** (salir y volver a entrar) para tomar efecto. El server cachea el access level en memoria.
