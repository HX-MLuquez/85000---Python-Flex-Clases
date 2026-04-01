# Unidad 13 - Cambios aplicados

Este documento resume en que archivo se aplico cada punto y que tener en cuenta.

## 01 - Creacion de la vista editar perfil

- Archivo: `user/views.py`
- Funcion agregada: `editarPerfil`
- Detalle: usa `EditProfileForm` con `instance=request.user` y requiere login.

## 02 - Creacion de la URL para editar perfil

- Archivo: `user/urls.py`
- Ruta agregada: `editarPerfil/`
- Nombre de URL: `EditarPerfil`
- Detalle: apunta a `views.editarPerfil`.

## 03 - Creacion del template de editar perfil

- Archivo: `user/templates/user/editar_perfil.html`
- Detalle: formulario POST con `{% csrf_token %}` y `{{ form.as_p }}`.

## 04 - Uso de UserChangeForm (form personalizado)

- Archivo: `user/forms.py`
- Clase agregada: `EditProfileForm(UserChangeForm)`
- Detalle: campos editables `email`, `first_name`, `last_name` con labels en espanol.

## 05 - Detalle de campos del formulario

- Archivo: `user/forms.py`
- Detalle: se restringen los campos para evitar exponer campos no necesarios del usuario.

## 06 - Gestion de avatares (modelo, vista, formulario, template, URL)

- Archivos:
  - `user/models.py`: clase `Avatar`
  - `user/forms.py`: clase `AvatarForm`
  - `user/views.py`: funcion `upload_avatar`
  - `user/urls.py`: ruta `upload-avatar/`
  - `user/templates/user/upload_avatar.html`: template de carga
- Detalle:
  - el modelo usa `ImageField(upload_to="avatares")`
  - la vista usa `get_or_create(user=request.user)` para evitar errores si no existe avatar.

## 07 - Configuracion de media

- Archivo: `AppCoder/settings.py`
- Configuracion agregada:
  - `MEDIA_URL = "/media/"`
  - `MEDIA_ROOT = BASE_DIR / "media"`

## 08 - Ajustes de URLs para media en desarrollo

- Archivo: `AppCoder/urls.py`
- Configuracion agregada:
  - import de `settings`, `static`
  - bloque condicional `if settings.DEBUG: urlpatterns += static(...)`

## 09 - Accesos en navegacion para probar cambios

- Archivo: `user/templates/user/base.html`
- Detalle: se agregaron links directos a `Editar Perfil` y `Subir Avatar`.

## 10 - Configuracion completa por variables de entorno

- Archivos:
  - `AppCoder/settings.py`
  - `.env`
  - `.env.prod`
- Detalle:
  - `settings.py` ahora carga variables desde archivo segun `DJANGO_ENV` (`development` o `production`).
  - se parametrizo `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, base de datos, estaticos y media.
  - se definieron valores de desarrollo en `.env`.
  - se definieron valores de produccion en `.env.prod` (plantilla lista para completar en Render).

## Consideraciones para produccion (especial estaticos y media)

- Django no debe servir estaticos ni media directamente en produccion.
- Configurar servidor web (Nginx/Apache) o plataforma cloud para servir:
  - carpeta de estaticos (resultado de `collectstatic`)
  - carpeta de media (subidas de usuarios)
- Comandos recomendados:
  - instalar Pillow (si no esta): `pip install Pillow`
  - aplicar migraciones: `python manage.py makemigrations` y `python manage.py migrate`
  - recopilar estaticos: `python manage.py collectstatic`
- Configuraciones recomendadas:
  - `DEBUG = False`
  - definir `ALLOWED_HOSTS`
  - usar variable de entorno para `SECRET_KEY`
  - definir `STATIC_ROOT` para `collectstatic`
  - mantener `MEDIA_ROOT` en un storage persistente (disco persistente o bucket S3 compatible)
- Si usas un proveedor cloud, revisar politica de persistencia del filesystem para no perder avatares en reinicios/despliegues.

## Deploy - paso a paso completo para Render

Esta guia asume que el proyecto Django a desplegar es `CLASE-13/AppCoder`.

### 1) Preparar el proyecto para produccion (local)

1. Crear y activar entorno virtual (si aun no lo tenes):
   - Windows (PowerShell):
     - `python -m venv .venv`
     - `.venv\Scripts\Activate.ps1`
   - Windows (Git Bash):
     - `python -m venv .venv`
     - `source .venv/Scripts/activate`

2. Instalar dependencias necesarias para deploy:
   - `pip install django gunicorn whitenoise dj-database-url psycopg[binary] pillow`

3. Generar `requirements.txt` actualizado:
   - `pip freeze > requirements.txt`

4. Crear archivo `build.sh` en la raiz de `AppCoder`:
   - Contenido sugerido:
   - `python manage.py collectstatic --noinput`
   - `python manage.py migrate`

5. Crear archivo `render.yaml` (opcional pero recomendado) o configurar todo desde UI.

### 2) Ajustes obligatorios de Django para produccion

Actualizar `AppCoder/settings.py`:

- Seguridad y entorno:
  - leer `SECRET_KEY` desde variable de entorno.
  - `DEBUG = False` en produccion.
  - `ALLOWED_HOSTS` con el dominio de Render (`*.onrender.com`) y tu dominio propio si aplica.
  - usar `CSRF_TRUSTED_ORIGINS` con URL HTTPS de Render.

- Base de datos:
  - usar `DATABASE_URL` con `dj_database_url`.
  - mantener SQLite para local si no hay `DATABASE_URL`.

- Estaticos:
  - definir:
    - `STATIC_URL = "/static/"`
    - `STATIC_ROOT = BASE_DIR / "staticfiles"`
  - agregar WhiteNoise:
    - en `MIDDLEWARE`, inmediatamente despues de `SecurityMiddleware`:
      - `"whitenoise.middleware.WhiteNoiseMiddleware"`
    - y opcional:
      - `STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"`

- Media (avatares):
  - mantener:
    - `MEDIA_URL = "/media/"`
    - `MEDIA_ROOT = BASE_DIR / "media"`
  - importante: en Render, el filesystem del servicio web no es persistente por defecto.
    - para no perder avatares, usar:
      - Disk persistente de Render (si tu plan lo permite), o
      - almacenamiento externo (S3/Cloudinary), recomendado para produccion real.

### 3) Archivos recomendados para Render

#### Procfile (recomendado)

Crear `Procfile` en raiz de `AppCoder`:

- `web: gunicorn AppCoder.wsgi:application`

#### runtime.txt (opcional)

Si queres fijar version de Python:

- `python-3.12.3`

#### .gitignore (verificar)

Asegurarte de ignorar:

- `.venv/`
- `__pycache__/`
- `db.sqlite3` (si no queres versionar base local)
- `media/` (si no corresponde subir archivos de usuario)

### 4) Subir codigo a GitHub

1. Verificar estado:
   - `git status`
2. Agregar cambios:
   - `git add .`
3. Commit:
   - `git commit -m "Preparar deploy en Render"`
4. Push:
   - `git push origin main`

### 5) Crear el servicio en Render

1. Ir a [https://render.com](https://render.com) y loguearte.
2. `New +` -> `Web Service`.
3. Conectar repositorio de GitHub.
4. Configurar:
   - Name: ejemplo `appcoder-django`
   - Region: la mas cercana
   - Branch: `main`
   - Runtime: `Python 3`
   - Build Command:
     - `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start Command:
     - `gunicorn AppCoder.wsgi:application`

### 6) Variables de entorno en Render (Environment)

Definir como minimo:

- `SECRET_KEY` = clave segura real
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = `tu-servicio.onrender.com`
- `CSRF_TRUSTED_ORIGINS` = `https://tu-servicio.onrender.com`

Si usas PostgreSQL en Render:

- crear `PostgreSQL` en Render
- copiar `External Database URL`
- agregar:
  - `DATABASE_URL` = `<url postgres>`

Opcionales recomendadas:

- `PYTHON_VERSION` = `3.12.3`
- `WEB_CONCURRENCY` = `2` (segun plan y memoria)

### 7) Base de datos: migraciones y superusuario

Render ejecuta migraciones si estan en Build Command.

Para crear superusuario:

1. Abrir `Shell` del servicio en Render.
2. Ejecutar:
   - `python manage.py createsuperuser`
3. Confirmar login en:
   - `https://tu-servicio.onrender.com/admin/`

### 8) Verificaciones post-deploy (checklist)

1. La home responde `200`.
2. Login/Register funcionan.
3. Edicion de perfil guarda cambios.
4. Subida de avatar funciona.
5. Admin carga CSS (si falla, problema de `collectstatic`/WhiteNoise).
6. Revisar logs de Render sin errores de import o migracion.

### 9) Consideraciones criticas para avatares (media) en Render

- Si guardas `MEDIA_ROOT` en disco local del contenedor:
  - los archivos pueden perderse en redeploy/restart.
- Soluciones:
  1. Render Disk persistente montado en ruta fija (si disponible).
  2. S3/Cloudinary con `django-storages` (mejor practica).

Si queres produccion robusta, priorizar S3/Cloudinary para `ImageField`.

### 10) Problemas comunes y solucion rapida

1. `DisallowedHost`:
   - falta dominio en `ALLOWED_HOSTS`.
2. Error CSRF en forms:
   - falta `CSRF_TRUSTED_ORIGINS` con `https://...onrender.com`.
3. CSS no carga:
   - no se ejecuto `collectstatic` o falta WhiteNoise.
4. `ModuleNotFoundError: gunicorn`:
   - agregar `gunicorn` a `requirements.txt`.
5. Migraciones no aplicadas:
   - agregar `python manage.py migrate` en Build Command.
6. Avatares desaparecen:
   - storage no persistente; mover a Disk persistente o S3/Cloudinary.

### 11) Comandos de referencia (resumen)

- Instalar dependencias deploy:
  - `pip install gunicorn whitenoise dj-database-url psycopg[binary] pillow`
- Exportar dependencias:
  - `pip freeze > requirements.txt`
- Migraciones:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Colectar estaticos:
  - `python manage.py collectstatic --noinput`
- Probar produccion local:
  - `set DEBUG=False` (cmd) o `$env:DEBUG="False"` (PowerShell)
  - `python manage.py runserver`

### 12) Deploy operativo exacto (en base a lo que YA tenes en este repo)

Esta es la secuencia concreta con `build.sh` + `render.yaml` actuales.

#### A. Lo que haces vos antes de Render

1. En la raiz `AppCoder`, generar dependencias:
   - `pip freeze > requirements.txt`
2. Verificar que esten en `requirements.txt` al menos:
   - `Django`
   - `gunicorn`
   - `whitenoise`
   - `Pillow`
   - `psycopg` o `psycopg-binary` (si DB Postgres)
3. Subir todo a GitHub:
   - `git add .`
   - `git commit -m "Config deploy Render con build.sh y render.yaml"`
   - `git push origin main`

#### B. Lo que configuras en Render (panel web)

1. Crear Web Service desde tu repo.
2. Render detecta `render.yaml` y toma:
   - `buildCommand: bash build.sh`
   - `startCommand: gunicorn AppCoder.wsgi:application`
3. En `Environment` completar variables sensibles (las que tienen `sync: false`):
   - `SECRET_KEY`
   - `DB_NAME`
   - `DB_USER`
   - `DB_PASSWORD`
   - `DB_HOST`
4. Confirmar valores no sensibles:
   - `DJANGO_ENV=production`
   - `DEBUG=False`
   - `DB_ENGINE=django.db.backends.postgresql`
   - `DB_PORT=5432`
   - `ALLOWED_HOSTS=<tu-servicio>.onrender.com`
   - `CSRF_TRUSTED_ORIGINS=https://<tu-servicio>.onrender.com`

#### C. Comandos que ejecuta Render automaticamente en cada deploy

Render corre exactamente este pipeline:

1. `bash build.sh`
2. Dentro de `build.sh` se ejecuta:
   - `python -m pip install --upgrade pip`
   - `pip install -r requirements.txt`
   - `python manage.py collectstatic --noinput`
   - `python manage.py migrate --noinput`
3. Luego levanta la app con:
   - `gunicorn AppCoder.wsgi:application`

#### D. Comandos manuales que podes ejecutar en Render Shell (solo si hace falta)

- Crear admin:
  - `python manage.py createsuperuser`
- Verificar chequeo Django:
  - `python manage.py check`
- Reaplicar migraciones manualmente (si hubo fallo puntual):
  - `python manage.py migrate --noinput`

#### E. Que NO tenes que ejecutar manualmente en Render

- No hace falta correr `collectstatic` a mano en cada deploy (ya lo hace `build.sh`).
- No hace falta correr `migrate` a mano en cada deploy (ya lo hace `build.sh`).
- No hace falta subir `.env.prod` al servidor; Render usa variables del panel.

---

---

---

## Producción en Render: usar una base de datos externa/persistente (PostgreSQL).

SQLite funciona para desarrollo local, pero en Render (Web Service) tiene limitaciones fuertes:

- El sistema de archivos del contenedor no es persistente entre deploys/restarts;
- Podés perder datos o tener inconsistencias;
- No escala bien para concurrencia real;
  no es una opción recomendada para producción.

Por eso te dejé .env con SQLite para desarrollo y .env.prod con PostgreSQL para producción.

### Respuesta corta

- Desarrollo local: SQLite está perfecto.
- Producción en Render: sí, es necesario/recomendado usar DB externa (ideal: PostgreSQL de Render).

### Qué conviene hacer en tu caso

- Crear una PostgreSQL en Render.
- Copiar sus datos de conexión a variables (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT) o usar DATABASE_URL.
- Ejecutar migraciones en deploy (python manage.py migrate).
- Mantener SQLite solo en local.
