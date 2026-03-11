# --- UNIDAD 11 - CODE ---
# Formularios en Django - Unidad 11: Playground Intermedio Parte II

from django import forms


# --- UNIDAD 11 - CODE ---
# Formulario para agregar un nuevo curso
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre del curso")
    camada = forms.IntegerField(label="Camada")


# --- UNIDAD 11 - CODE ---
# Formulario de búsqueda de cursos por camada
class BusquedaCursoFormulario(forms.Form):
    camada = forms.IntegerField(label="Camada")
