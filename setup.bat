@echo off

REM Verifica se o Python 3 está instalado
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python3 não encontrado. Por favor, instale manualmente:
    echo   Baixe em https://www.python.org/downloads/
    echo Depois de instalar, execute este script novamente.
    exit /b 1
)

echo.
echo ========================================
echo Configurando o ambiente virtual
echo ========================================

REM Cria o ambiente virtual se não existir
if not exist .venv (
    echo Criando .venv...
    python -m venv .venv
) else (
    echo .venv já existe, reaproveitando o ambiente
)

REM Ativa o ambiente virtual
call .\.venv\Scripts\activate.bat

REM Atualiza o pip
python -m pip install --upgrade pip

REM Instala as dependências se o arquivo requirements.txt existir e não estiver vazio
if exist requirements.txt (
    for /f %%i in ('findstr /r /c:"." requirements.txt') do (
        echo Instalando dependências...
        python -m pip install -r requirements.txt -q
        goto :done
    )
    echo requirements.txt está vazio; pulando instalação de dependências
) else (
    echo requirements.txt não encontrado; pulando instalação de dependências
)

:done
echo.
echo ========================================
echo Setup concluído. Para usar python no venv neste terminal, execute:
echo call .\.venv\Scripts\activate.bat
echo ========================================