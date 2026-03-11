from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("probando/", views.probando_template, name="probando"),
    path("cursos/", views.cursos, name="cursos"),
    path("cursoFormulario/", views.cursoFormulario, name="cursoFormulario"),
    path("buscarCurso", views.buscarCurso, name="buscarCurso"),
]
