@echo off
title L2 Meraki - Panel de Control
echo ==========================================
echo        Iniciando Servidores L2 Meraki
echo ==========================================
echo.
echo Iniciando Login Server...
start "Meraki Login Server" cmd /k "cd /d server_data\login && "C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot\bin\java.exe" -server -Dfile.encoding=UTF-8 -Dorg.slf4j.simpleLogger.log.com.zaxxer.hikari=warn -XX:+UseZGC -Xms128m -Xmx256m -jar ../libs/LoginServer.jar"

timeout /t 3 >nul

echo Iniciando Game Server...
start "Meraki Game Server" cmd /k "cd /d server_data\game && "C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot\bin\java.exe" -server -Dfile.encoding=UTF-8 -Djava.util.logging.manager=org.l2jmobius.log.ServerLogManager -Dorg.slf4j.simpleLogger.log.com.zaxxer.hikari=warn -XX:+UseZGC -Xmx2g -Xms512m -jar ../libs/GameServer.jar"

echo.
echo Servidores iniciados en ventanas separadas.
echo Ya puedes cerrar esta ventanita.
exit
