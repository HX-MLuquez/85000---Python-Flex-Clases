from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("probando/", views.probando_template, name="probando"),
]