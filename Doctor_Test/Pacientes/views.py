from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render (request, 'Index.html')

def registro(request):
    return render (request, 'crear.html')

def actualizar(request):
    return render (request, 'editar.html')

def eliminar(request):
    return render (request, 'eliminar.html')