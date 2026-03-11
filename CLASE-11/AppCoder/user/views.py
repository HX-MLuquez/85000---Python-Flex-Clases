from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario, BusquedaCursoFormulario


# * Ejemplo de CARGA DE TEMPLATE MANUAL
def inicio(request):
    template = loader.get_template("user/inicio.html")
    return HttpResponse(template.render())


def probando_template(request):
    contexto = {
        "nom": "Juan",
        "ap": "Perez",
        "notas": [10, 7, 3, 9],
    }
    return render(request, "user/probando.html", contexto)


def cursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "user/cursos.html", contexto)


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
