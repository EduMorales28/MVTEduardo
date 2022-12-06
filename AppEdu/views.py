from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def familiar(request):
    juan = Familiar(nombre = "Juan", apellido = "Perez", edad = 22, fechaNacimiento = 10/12/2000)
    romina = Familiar(nombre = "Romina", apellido = "Martinez", edad = 40, fechaNacimiento = 10/12/1982)
    martin = Familiar(nombre = "Martin", apellido = "Pereira", edad = 20, fechaNacimiento = 10/12/2022)
    
    juan.save()
    romina.save()
    martin.save()

    cadena = f"Familiares guardados"
    return HttpResponse(cadena)