# --- UNIDAD 11 - CODE ---
# Formularios en Django - Unidad 11: Playground Intermedio Parte II

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar


# --- UNIDAD 11 - CODE ---
# Formulario para agregar un nuevo curso
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre del curso")
    camada = forms.IntegerField(label="Camada")


# --- UNIDAD 11 - CODE ---
# Formulario de búsqueda de cursos por camada
class BusquedaCursoFormulario(forms.Form):
    camada = forms.IntegerField(label="Camada")


# -- CODE - Parte III ---
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)


# -- CODE - Parte III ---
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


# clase final - 04 uso de UserChangeForm
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
        labels = {
            "email": "Correo Electronico",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }


# clase final - 05 creacion del formulario de avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]
