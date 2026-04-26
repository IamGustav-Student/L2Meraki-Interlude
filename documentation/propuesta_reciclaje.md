# Propuesta Técnica: Sistema de Reciclaje Meraki

Este plan detalla la implementación de una función de "Venta Rápida / Reciclaje" accesible desde el Community Board (Merchant). Dado que el cliente no permite de forma nativa el uso de `Ctrl+Alt+Click` sin mods complejos, esta solución utiliza la infraestructura del servidor para ofrecer una experiencia similar y eficiente.

## 1. Interfaz de Usuario (HTML)
Se añadirá una nueva pestaña llamada **"Reciclaje"** en el menú del Merchant.

- **Vista de Inventario**: Una lista dinámica que muestra los ítems vendibles del jugador.
- **Botones de Acción**:
    - `[Reciclar]`: Vende el ítem individualmente.
    - `[Reciclar Todo]`: Vende todos los ítems marcados como "basura" (opcional).
- **Feedback Visual**: El jugador verá cuánta Adena o Cristales recibirá antes de confirmar.

## 2. Lógica del Servidor (Java)
Implementaremos un nuevo `Bypass` en el motor del Community Board:

- **Detección de Precio**: El sistema consultará el `sellPrice` definido en el servidor para cada ítem.
- **Lógica de Cristales**: Si el ítem es Grado D, C, B, A o S y tiene definido un `crystal_type`, el sistema calculará la cantidad de cristales basándose en la configuración de cristalización estándar.
- **Validación de Seguridad**:
    - No se podrán reciclar ítems equipados.
    - No se podrán reciclar ítems de misión o especiales.
    - Confirmación antes de reciclar ítems Grado S.

## 3. Flujo de Trabajo
1. El jugador abre el Community Board -> Merchant -> Reciclaje.
2. El servidor envía el HTML con la lista de ítems vendibles.
3. El jugador hace click en "Reciclar".
4. El servidor procesa el bypass:
    - Borra el ítem del inventario.
    - Añade la Adena o los Cristales correspondientes.
    - Refresca la ventana de Reciclaje.

## Preguntas Abiertas
- ¿Prefieres que el sistema devuelva **Adena** para todo, o **Cristales** específicamente para el equipo de grado alto?
- ¿Quieres un botón de "Reciclaje Automático" que limpie ítems comunes de bajo valor (pociones vacías, materiales comunes, etc.)?
