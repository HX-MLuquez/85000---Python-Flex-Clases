# DJANGO - CARACTERISTICAS PRINCIPALES
JUNTAMOS CSS HTML + CLASES + DJANGO (framework)
```
MODELS  VIEWS (lógica)  URLS (ROUTES)  TEMPLATES  +  STATIC -> CSS HTML JS 

DJANGO CONTIENE MÓDULOS de SEGURIDAD + MOTOR de PLANTILLAS JINJA + ORM + SERVER LISTEN + ...

USAREMOS CLASS (clases) y DEF (funciones)
```
# Introducción a Django

## Qué es un framework

Un framework es una estructura o plataforma de software que proporciona una base sobre la cual se puede desarrollar software. Ofrece un conjunto de herramientas, bibliotecas y convenciones para facilitar el desarrollo de aplicaciones, permitiendo a los desarrolladores centrarse en la lógica de la aplicación en lugar de en detalles de bajo nivel.

## ¿Qué aprenderemos en este módulo?

Construir aplicaciones Web empresariales utilizando el patrón MVT (MVC) en el entorno de desarrollo Python/Django para dar solución a los requerimientos de la organización.

- Unidad 1: Introducción a Django
- Unidad 2: Creación de un proyecto Python Django


## ¿Qué aprenderás en esta sesión?

- Reconocer las características de Django y su utilidad para el desarrollo de aplicaciones empresariales bajo el entorno Python.

## ¿Recuerdas qué es una librería en programación?

Una librería en programación es un conjunto de funciones, clases o módulos predefinidos que se pueden utilizar en el desarrollo de software para realizar tareas comunes sin tener que escribir el código desde cero.

## ¿Sabes qué es un Framework?

Un framework es una estructura predefinida que proporciona un entorno de trabajo estándar para desarrollar aplicaciones de software. Facilita la creación de aplicaciones al ofrecer componentes reutilizables y una arquitectura definida.

### Características de Django

Django es un framework de alto nivel para el desarrollo de aplicaciones web en Python que promueve el desarrollo rápido y un diseño limpio y pragmático. Algunas de sus características clave son:

- **Rapidez en el desarrollo**: Permite a los desarrolladores construir aplicaciones rápidamente gracias a sus múltiples herramientas integradas.
- **Seguridad**: Incluye medidas de seguridad integradas que ayudan a proteger las aplicaciones contra vulnerabilidades comunes.
- **Escalabilidad**: Facilita la creación de aplicaciones escalables que pueden crecer con el tiempo.
- **Versatilidad**: Django puede utilizarse para desarrollar una amplia gama de aplicaciones, desde sitios web pequeños hasta aplicaciones web complejas.

### Ejemplo de un Proyecto Django

A continuación, se muestra un ejemplo simple de cómo se crea un proyecto en Django:

**Previo INSTALL DJANGO dentro de nuestro VE, siempre confirmar tener la última versión de nuestro manejador de paquetes (dependencias) `PIP`**

Teniendo ACTIVATE nuestro entorno virtual. Antes debemos asegurarnos que tenemos la última versión de pip, que en definitiva es el software que utilizamos para instalar Django:
(venv)

```bash
pip --version
```


Si estás usando **Pipenv**, el flujo cambia un poco respecto a `pip` “normal”. No necesitás activar manualmente un `venv` tradicional: Pipenv crea y gestiona su propio entorno.

Te lo ordeno claro y simple 👇

---

## 1️⃣ Verificar que estás dentro del entorno de Pipenv

Entrá al entorno con:

```bash
pipenv shell
```

Si ya estás dentro, podés comprobar la versión de Python:

```bash
python --version
```

---

## 2️⃣ Instalar Django con Pipenv

En lugar de:

```bash
pip install django
```

Usás:

```bash
pipenv install django
```

Eso:

* Instala Django
* Crea/actualiza el `Pipfile`
* Crea el entorno virtual si no existe

---

## 3️⃣ Ejecutar comandos dentro de Pipenv

Tenés dos opciones:

### ✔ Opción A — Entrar al shell

```bash
pipenv shell
```
* Verificar con:
```bash
python --version
where python
```

```bash
pipenv install django
django-admin startproject myproject .
```

### ✔ Opción B — Sin entrar al shell

```bash
pipenv run django-admin startproject myproject
```

---

## 4️⃣ Ejecutar el servidor

Si estás dentro del shell:

```bash
cd myproject
python manage.py runserver
```

Si no:

```bash
pipenv run python manage.py runserver
```

```bash
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 24, 2026 - 16:34:39
Django version 6.0.2, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server        instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
```

* Para solucionar el warning de las migraciones pendientes:
```bash
python manage.py migrate
```


---

## 5️⃣ Sobre `pip --version` y `upgrade pip`

Si estás usando Pipenv, no necesitás hacer:

```bash
python -m pip install --upgrade pip
```

Porque:

* Pipenv ya gestiona las dependencias
* El `pip` interno pertenece al entorno virtual que Pipenv crea

Si querés ver el pip del entorno:

```bash
pipenv run pip --version
```

---

Perfecto 👌 Te armo algo simple y claro para levantar una app con **Django + Pipenv**, con:

* ✅ Home
* ✅ Card centrada
* ✅ Click en la card → vista detalle

---

# 🚀 1️⃣ Crear entorno con Pipenv

```bash
# Crear carpeta del proyecto
mkdir mi_proyecto
cd mi_proyecto

# Crear entorno con Django
pipenv install django

# Activar entorno
pipenv shell
```

---

# 🏗 2️⃣ Crear proyecto y app

```bash
# Crear proyecto
django-admin startproject config .

# Crear app
python manage.py startapp core
```