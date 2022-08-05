from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

def saludo(request):
    return HttpResponse('hola mundo')

def canelones(request):
    return HttpResponse('canelones de carne')

def dia_de_hoy(request):
    hoy=datetime.today().date()
    return HttpResponse(f'hoy es{hoy}')

def saludo_con_nombre(request, nombre):
        return HttpResponse(f'Hola queridisimo {nombre}')

def año_de_nacimiento(request, edad):
    año_actual = datetime.today().year
    nacimiento = año_actual- edad
    return HttpResponse(f'naciste en el año {nacimiento}')


def plantilla(request):
    return render(request, 'plantilla.html', context={})




    




