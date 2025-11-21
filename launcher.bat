@echo off
:: ========================================
:: WhatsApp Converter Premium - Launcher
:: BS Developer
:: ========================================

title WhatsApp Converter Premium - Launcher
color 0D
cls

echo.
echo ========================================
echo    WhatsApp Converter Premium
echo    BS Developer - Launcher
echo ========================================
echo.

:menu
echo Escolha uma opcao:
echo.
echo [1] Abrir Site Principal
echo [2] Abrir Showcase de Features
echo [3] Iniciar Servidor Local (porta 8000)
echo [4] Converter Logo para Base64
echo [5] Ver Documentacao
echo [0] Sair
echo.
set /p opcao="Digite o numero da opcao: "

if "%opcao%"=="1" goto site
if "%opcao%"=="2" goto showcase
if "%opcao%"=="3" goto servidor
if "%opcao%"=="4" goto base64
if "%opcao%"=="5" goto docs
if "%opcao%"=="0" goto fim
goto menu

:site
cls
echo.
echo Abrindo WhatsApp Converter Premium...
start whatsapp-converter-premium.html
echo.
echo Site aberto no navegador!
echo.
pause
goto menu

:showcase
cls
echo.
echo Abrindo Showcase de Features...
start showcase.html
echo.
echo Showcase aberto no navegador!
echo.
pause
goto menu

:servidor
cls
echo.
echo Iniciando servidor local na porta 8000...
echo.
echo IMPORTANTE: Deixe esta janela aberta!
echo Acesse: http://localhost:8000
echo.
echo Pressione Ctrl+C para parar o servidor.
echo.
python -m http.server 8000
pause
goto menu

:base64
cls
echo.
echo Conversor de Logo para Base64
echo.
set /p logopath="Digite o caminho da imagem (ex: logo.png): "
echo.
echo Convertendo...
python image-to-base64.py "%logopath%"
echo.
pause
goto menu

:docs
cls
echo.
echo ========================================
echo    Documentacao Disponivel
echo ========================================
echo.
echo [1] README.md - Indice geral
echo [2] README-FEATURES.md - Docs tecnicas
echo [3] GUIA-RAPIDO.md - Tutorial rapido
echo.
set /p docsopcao="Qual arquivo deseja abrir? "

if "%docsopcao%"=="1" start README.md
if "%docsopcao%"=="2" start README-FEATURES.md
if "%docsopcao%"=="3" start GUIA-RAPIDO.md

echo.
pause
goto menu

:fim
cls
echo.
echo Obrigado por usar WhatsApp Converter Premium!
echo Desenvolvido com amor por BS Developer
echo.
timeout /t 2 >nul
exit