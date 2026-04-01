# --- UNIDAD 11 - CODE ---
# Vistas - Unidad 11: Playground Intermedio Parte II

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Curso, Estudiante, Profesor, Entregable
from .forms import (
    CursoFormulario,
    BusquedaCursoFormulario,
    RegistroUsuarioForm,
    EditProfileForm,
    AvatarForm,
)
from .models import Avatar


# --- UNIDAD 11 - CODE ---
# Vista de inicio
@login_required
def inicio(request):
    template = loader.get_template("user/inicio.html")
    return HttpResponse(template.render())


# --- UNIDAD 11 - CODE ---
# Vista de prueba de template (existente)
def probando_template(request):
    contexto = {
        "nom": "Juan",
        "ap": "Perez",
        "notas": [10, 7, 3, 9],
    }
    return render(request, "user/probando.html", contexto)


# --- UNIDAD 11 - CODE ---
# Vista de página de cursos
def cursos(request):
    # Buscamos todos los cursos en la base de datos
    cursos = Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, "user/cursos.html", context)


# --- UNIDAD 11 - CODE ---
# Vista de página de profesores
def profesores(request):
    return render(request, "user/profesores.html")


# --- UNIDAD 11 - CODE ---
# Vista de página de estudiantes
def estudiantes(request):
    return render(request, "user/estudiantes.html")


# --- UNIDAD 11 - CODE ---
# Vista de página de entregables
def entregables(request):
    return render(request, "user/entregables.html")


# --- UNIDAD 11 - CODE ---
# Vista para el formulario de agregar curso (GET y POST)
def cursoFormulario(request):
    if request.method == "POST":
        form = CursoFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            camada = form.cleaned_data["camada"]
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
            return render(request, "user/curso_exito.html")
    else:
        form = CursoFormulario()
    return render(request, "user/curso_formulario.html", {"form": form})


# --- UNIDAD 11 - CODE ---
# Vista para buscar curso por camada (Búsqueda con formularios)
def buscarCurso(request):
    if request.method == "GET":
        form = BusquedaCursoFormulario(request.GET)
        if form.is_valid():
            camada = form.cleaned_data["camada"]
            resultados = Curso.objects.filter(camada=camada)
            return render(
                request,
                "user/resultados_busqueda.html",
                {"resultados": resultados, "form": form},
            )
    else:
        form = BusquedaCursoFormulario()
    return render(request, "user/buscar_curso.html", {"form": form})


class ProfesorList(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "user/leer_profesores.html"
    context_object_name = "profesores"


class ProfesorCrear(LoginRequiredMixin, CreateView):
    model = Profesor
    fields = ["nombre", "apellido", "email", "profesion"]
    template_name = "user/profesores_form.html"
    success_url = reverse_lazy("profesores_list")


class ProfesorEditar(LoginRequiredMixin, UpdateView):
    model = Profesor
    fields = ["nombre", "apellido", "email", "profesion"]
    template_name = "user/editar_profesor.html"
    success_url = reverse_lazy("profesores_list")


class ProfesorBorrar(LoginRequiredMixin, DeleteView):
    model = Profesor
    template_name = "user/profesor_confirm_delete.html"
    success_url = reverse_lazy("profesores_list")


# -- CODE - Parte III ---
class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "user/curso_list.html"
    context_object_name = "cursos"

'''
context = {}
context = {"cursos": cursos}
'''



# -- CODE - Parte III --- DetailView por defecto espera un id por params (url)
class CursoDetalle(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "user/curso_detalle.html"


# -- CODE - Parte III ---
class CursoCrear(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ["nombre", "camada"]
    template_name = "user/curso_form.html"
    success_url = reverse_lazy("curso_list")


# -- CODE - Parte III --- UpdateView por defecto espera un id por params (url)
class CursoEditar(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ["nombre", "camada"]
    template_name = "user/curso_form.html"
    success_url = reverse_lazy("curso_list")


# -- CODE - Parte III --- DeleteView por defecto espera un id por params (url)
class CursoBorrar(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = "user/curso_confirm_delete.html"
    success_url = reverse_lazy("curso_list")
    
# -- CODE - Parte III --- Soft delete (desactivar en lugar de eliminar)
'''
class CursoBorrar(LoginRequiredMixin, updateView):
    model = Curso
    fields = ["activo"] # Campo booleano agregado en migración posterior
    template_name = "user/curso_confirm_delete.html"
'''


# -- CODE - Parte III ---
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})


# -- CODE - Parte III ---
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistroUsuarioForm()
    return render(request, "user/register.html", {"form": form})


# clase final - 01 creacion de la vista editar perfil
@login_required
def editarPerfil(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "user/editar_perfil.html", {"form": form})


# clase final - 04 creacion de la vista para gestionar avatares
@login_required
def upload_avatar(request):
    avatar, _ = Avatar.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AvatarForm(instance=avatar)
    return render(request, "user/upload_avatar.html", {"form": form, "avatar": avatar})

'''
Login y Register con cbv 
class LoginView(auth_views.LoginView):
    template_name = "user/login.html"
    
class RegisterView(CreateView):
    template_name = "user/register.html"
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy("login")
'''
