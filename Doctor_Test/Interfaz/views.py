from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


def interfaz(request):
    return render(request, 'index.html')

@login_required
def plataforma(request):
    return render(request, 'plataforma.html')

@login_required
def pacientes(request):
    response = requests.get('http://127.0.0.1:8000/pacientes/api/api/paciente/')
    pacientes = response.json()
    return render(request, 'pacientes.html',  {'pacientes': pacientes})

