#!/usr/bin/env bash

# clase final - 20 script de build para Render
# Detiene el script ante cualquier error.
set -o errexit

# clase final - Actualiza pip por compatibilidad de dependencias
python -m pip install --upgrade pip

# clase final - Instala dependencias del proyecto
pip install -r requirements.txt

# clase final - Recopila archivos estaticos para produccion
python manage.py collectstatic --noinput

# clase final - Aplica migraciones de base de datos
python manage.py migrate --noinput