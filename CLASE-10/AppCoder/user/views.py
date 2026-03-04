from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


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
