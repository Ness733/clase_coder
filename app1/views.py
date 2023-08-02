from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
import datetime
from .models import Curso

# Create your views here.


def probando_template(request):

    nombre = "Luis"
    apellido = "Perez"
    lista_de_notas = [1, 2, 3, 5, 8, 3, 2]

    diccionario = {"nombre": nombre, "apellido": apellido,
                   "hoy": datetime.datetime.now(), "notas": lista_de_notas}

    plantilla = loader.get_template(
        "template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso': curso})


def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_comision = request.POST.get('numero_comision')
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect('/app1/curso_list/', foo="bar")
    return render(request, 'curso_create.html')


def index(request):
    return render(request, "index.html")
