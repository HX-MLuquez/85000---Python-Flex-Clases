def registrar_usuario(nombre, edad):
    """
    Registra un nuevo usuario con su nombre y edad.
    """
    usuario = {
        'nombre': nombre,
        'edad': edad
    }
    return usuario

# ---------------------------------------------------

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_USUARIOS = os.path.join(SCRIPT_DIR, "usuarios.txt")
usuarios = {}
def cargar_usuarios_desde_archivo():
    """Función para cargar usuarios desde el archivo de texto en Drive"""
    try:
        # verificar_directorio()

        if not os.path.exists(ARCHIVO_USUARIOS):
            print(
                f"Archivo no encontrado. Se creará uno nuevo en: {ARCHIVO_USUARIOS}")
            with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as archivo:
                pass
            return

        with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                if linea:
                    partes = linea.split(':')
                    if len(partes) == 2:
                        usuario, contraseña = partes
                        usuarios[usuario] = contraseña

            print(f"Se cargaron {len(usuarios)} usuarios desde el archivo.")

    except Exception as e:
        print(f"Error al cargar usuarios desde archivo: {e}")
