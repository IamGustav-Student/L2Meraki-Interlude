@echo off
title L2 Meraki - Client Cleaner
echo --- Iniciando limpieza de archivos corruptos (Crack Shot / Raccoon) ---

:: 1. Eliminar de Animations
echo Limpiando Animations...
del /s /q Animations\*CrackShot* 2>nul
del /s /q Animations\*Raccoon* 2>nul

:: 2. Eliminar de SysTextures
echo Limpiando SysTextures...
del /s /q SysTextures\*CrackShot* 2>nul
del /s /q SysTextures\*Raccoon* 2>nul

:: 3. Eliminar de system
echo Limpiando system...
del /s /q system\*CrackShot* 2>nul
del /s /q system\*Raccoon* 2>nul

:: 4. Resetear opciones
if exist system\Option.ini (
    echo Reseteando Option.ini...
    del /q system\Option.ini
)

echo.
echo --- LIMPIEZA COMPLETADA ---
echo Ya puedes abrir el juego sin crashes.
pause
