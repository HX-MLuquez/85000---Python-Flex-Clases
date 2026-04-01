# --- UNIDAD 11 - CODE ---
# Panel de Administración - Unidad 11: Playground Intermedio Parte II

from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Entregable


# --- UNIDAD 11 - CODE ---
# Personalización del administrador para Curso
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "camada")
    search_fields = ("nombre",)
    list_filter = ("camada",)


# --- UNIDAD 11 - CODE ---
# Personalización del administrador para Estudiante
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email")
    search_fields = ("nombre", "apellido", "email")
    list_filter = ("nombre",)


# --- UNIDAD 11 - CODE ---
# Personalización del administrador para Profesor
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email", "profesion")
    search_fields = ("nombre", "apellido", "profesion")
    list_filter = ("profesion",)


# --- UNIDAD 11 - CODE ---
# Personalización del administrador para Entregable
class EntregableAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_de_entrega", "entregado")
    search_fields = ("nombre",)
    list_filter = ("entregado",)


# --- UNIDAD 11 - CODE ---
# Registro de modelos en el panel de administración
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregableAdmin)
