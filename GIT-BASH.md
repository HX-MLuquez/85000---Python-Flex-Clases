# Instalar Git Bash  

1. Descarga Git Bash: Ve al sitio web oficial de Git (https://git-scm.com/) y descarga la versión correspondiente a tu sistema operativo (Windows, macOS o Linux).

2. Instalación: Ejecuta el instalador descargado y sigue las instrucciones del asistente de instalación. Asegúrate de marcar la opción para incluir Git Bash en el PATH del sistema si estás en Windows.

## Configurar Git en Visual Studio Code:
1. Instalar Visual Studio Code: Si aún no lo tienes, descarga e instala Visual Studio Code desde su sitio web oficial (https://code.visualstudio.com/).

2. Instalar la extensión Git: Abre Visual Studio Code, ve a la pestaña de Extensiones (Ctrl+Shift+X), busca "Git" y haz clic en "Install" para instalar la extensión de Git.

## Configurar la ruta de Git Bash en VSC:

1. Abre Visual Studio Code.

Ve a "File" > "Preferences" > "Settings" (o simplemente presiona Ctrl+,).

2. En la barra de búsqueda, escribe "git path".
3. Busca la configuración llamada "Git: Path" y haz clic en "Edit in settings.json".
4. Agrega la ruta de instalación de Git Bash. Por ejemplo, en Windows, la ruta predeterminada podría ser algo como: 
```bash
"git.path": "C:\\Program Files\\Git\\bin\\git.exe". Asegúrate de que la ruta coincida con la ubicación donde instalaste Git en tu sistema.
```

5. Reiniciar Visual Studio Code: Es posible que necesites cerrar y volver a abrir Visual Studio Code para que los cambios surtan efecto.