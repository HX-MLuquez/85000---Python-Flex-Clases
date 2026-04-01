# 🧩 📘 Proyecto Final Django – Blog (estructura completa)

## 🎯 Objetivo

Crear una aplicación web tipo blog con:

- Autenticación de usuarios
- CRUD de páginas/posts
- Perfiles
- Mensajería
- Deploy listo

---

# 🏗️ Estructura del proyecto

```bash
mi_proyecto/
│
├── mi_proyecto/       # configuración principal
├── blog/              # app principal (pages)
├── accounts/          # usuarios        # mensajes
├── static/
├── media/
├── templates/
├── manage.py
├── requirements.txt
└── .gitignore
```

---

# 📌 Funcionalidades obligatorias

## 🏠 Home

- Ruta: `/`
- Vista simple de bienvenida

---

## 👤 About

- Ruta: `/about/`
- Información del dueño

---

## 📝 Pages (Blog)

### 📍 Rutas

- `/pages/` → listado
- `/pages/<id>/` → detalle
- `/pages/create/` → crear
- `/pages/update/<id>/` → editar
- `/pages/delete/<id>/` → borrar

---

## Modelo principal (ej: Post)

Debe tener mínimo:

```python
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    contenido = RichTextField()  # ckeditor
    imagen = models.ImageField(upload_to='posts/')
    fecha = models.DateField(auto_now_add=True)
```

---

## 📄 Listado (pages)

- Mostrar resumen de cada post
- Botón “Leer más” → detalle

👉 Si no hay posts:

```html
No hay páginas aún
```

---

## 🔍 Detalle

- Muestra toda la info del post

---

## 🔒 Restricciones

✔️ Crear / editar / borrar → solo usuarios logueados
✔️ Usar:

- `LoginRequiredMixin` (CBV)
- `@login_required` (FBV)

---

# 👤 Accounts (usuarios)

## Funcionalidades

- Login → `/login/`
- Signup → `/signup/`
- Logout → `/logout/`
- Perfil → `/profile/`
- Editar perfil

---

## Perfil (modelo extendido)

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
```

---

## 📄 Vista perfil

Mostrar:

- Nombre
- Apellido
- Email
- Avatar
- Bio

---

# 🎨 Templates

## ✔️ Herencia obligatoria

### `base.html`

Debe incluir:

- Navbar con:
  - Home
  - About
  - Pages
  - Login / Logout
  - Profile

```html
{% block content %}{% endblock %}
```

---

# CBV obligatorias

Mínimo 2:

Ejemplo:

```python
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
```

---

# 🔐 Mixin obligatorio

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
```

---

# 🔒 Decorador obligatorio

```python
from django.contrib.auth.decorators import login_required

@login_required
def mi_vista(request):
    ...
```

---

# 🧾 Forms con imágenes

⚠️ IMPORTANTE:

```html
<form method="POST" enctype="multipart/form-data"></form>
```

---

# ⚙️ Admin

Registrar todos los modelos en `admin.py`:

```python
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Message)
```

---

# 📦 requirements.txt

```bash
Django
gunicorn
whitenoise
dj-database-url
psycopg[binary]
pillow
django-ckeditor
```

---

# 🚫 .gitignore

```bash
__pycache__/
db.sqlite3
media/
```

---

# 📹 Entrega

## ✔️ Obligatorio

- Repo en GitHub
- README (como entrega anterior)
- Video ≤ 10 min mostrando:
  - navegación
  - CRUD
  - login
  - perfil
  - mensajes

---

# ⚠️ Cosas IMPORTANTES que evalúan

✔️ Funcione TODO
✔️ No haya errores
✔️ Código ordenado
✔️ Navegación clara
✔️ Mensaje “No hay páginas aún”
✔️ Login requerido donde corresponde

---

# 🚀 Recomendación final (clave)

Antes de entregar:

- Probá:
  - crear post
  - editar
  - borrar
  - login/logout
  - subir imagen
  - ver perfil
  - enviar mensaje

👉 TODO sin errores

---

# Hacer un breve video mostrando TODO lo que pide la consigna
- Navegación
- CRUD
- Login/logout
- Perfil


# EXTRAS - Si querés subir nivel (EXTRAS, no es obligatorio, pero suma puntos)

- Likes ❤️
- Buscador 🔍
- Paginación
- Deploy en Render

---

postgresql://app_db_render_user:i1yZUtWN7SUnyV9rgkB8OocaKxLaN74U@dpg-d765nqn5r7bs73c0577g-a/app_db_render

