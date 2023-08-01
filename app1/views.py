from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime

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


def template_model(request):

    nombre = "Luis"
    apellido = "Perez"
    lista_de_notas = [1, 2, 3, 5, 8, 3, 2]

    diccionario = {"nombre": nombre, "apellido": apellido,
                   "hoy": datetime.datetime.now(), "notas": lista_de_notas}

    plantilla = loader.get_template("template_model.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
