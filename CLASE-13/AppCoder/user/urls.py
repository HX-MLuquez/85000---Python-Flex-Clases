# --- UNIDAD 11 - CODE ---
# URLs - Unidad 11: Playground Intermedio Parte II - Navegación entre Templates

from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("cursos/", views.cursos, name="cursos"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("entregables/", views.entregables, name="entregables"),
    path("cursoFormulario/", views.cursoFormulario, name="cursoFormulario"),
    path("buscarCurso/", views.buscarCurso, name="buscarCurso"),
    path("probando/", views.probando_template, name="probando"),
    # -- CODE - Parte III ---
    path("profesores/", views.ProfesorList.as_view(), name="profesores_list"),
    path("profesores/crear/", views.ProfesorCrear.as_view(), name="profesores_crear"),
    path(
        "profesores/borrar/<int:pk>/",
        views.ProfesorBorrar.as_view(),
        name="profesores_eliminar",
    ),
    path(
        "profesores/editar/<int:pk>/",
        views.ProfesorEditar.as_view(),
        name="profesores_editar",
    ),
    # -- CODE - Parte III ---
    path("cursos-list/", views.CursoList.as_view(), name="curso_list"),
    path("cursos/<int:pk>/", views.CursoDetalle.as_view(), name="curso_detalle"),
    path("cursos/crear/", views.CursoCrear.as_view(), name="curso_crear"),
    path("cursos/editar/<int:pk>/", views.CursoEditar.as_view(), name="curso_editar"),
    path("cursos/borrar/<int:pk>/", views.CursoBorrar.as_view(), name="curso_borrar"),
    # -- CODE - Parte III ---
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path(
        "logout",
        LogoutView.as_view(template_name="user/logout.html"),
        name="logout",
    ),
    # clase final - 02 creacion de la url para editar perfil
    path("editarPerfil/", views.editarPerfil, name="EditarPerfil"),
    # clase final - 04 creacion de la url para cargar avatar
    path("upload-avatar/", views.upload_avatar, name="upload_avatar"),
    # '''
    # Traer los path nativos de Django para Login, Logout y Register. Para Logout usar la vista LogoutView de Django, y para Login y Register crear las vistas en views.py (login_request y register respectivamente) y luego mapearlas aquí.
    # '''
    
]
