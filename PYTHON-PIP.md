# Python + Pip

## Instalación de Python

1. Descarga el instalador de Python desde la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Ejecuta el instalador y asegúrate de marcar la opción "Add Python to PATH" antes de hacer clic en "Install Now".
3. Verifica la instalación abriendo una terminal (CMD o PowerShell en Windows, Terminal

## Instalación de Pip

1. Pip generalmente se instala automáticamente con Python. Para verificar si Pip está instalado, abre una terminal y ejecuta:
   ```
   pip --version
   ```
2. Si Pip no está instalado, puedes descargar el script `get-pip.py` desde [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py). en macOS/Linux) y ejecutando:
   ```
    python --version
   ```
   python get-pip.py
3. Verifica la instalación de Pip ejecutando:
   ```
   pip --version
   ```

Y en windows:

```
python -m pip --version
```

* Solución del PATH en caso de que no funcione python:
- Ir a "Panel de Control" -> "Sistema y Seguridad" -> "Sistema" -> "Configuración avanzada del sistema" -> "Variables de entorno".
- En "Variables del sistema", selecciona la variable "Path" y haz clic en "Editar".
- Añade la ruta donde se instaló Python (por ejemplo, `C:\Python39\` y `C:\Python39\Scripts\`) y guarda los cambios.

20:23 volvemos!


y para Instalar pip:

```
python -m ensurepip --upgrade
```

## Uso Básico de Pip

- Para instalar un paquete:

  ```
  pip install nombre_del_paquete
  ```

- Para desinstalar un paquete:
  ```
  pip uninstall nombre_del_paquete
  ```
