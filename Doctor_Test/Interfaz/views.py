from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests


def interfaz(request):
    return render(request, 'index.html')

@login_required
def plataforma(request):
    return render(request, 'plataforma.html')

@login_required
def pacientes(request):
    response = requests.get('http://127.0.0.1:8000/pacientes/api/paciente/')
    pacientes = response.json()
    return render(request, 'pacientes.html',  {'pacientes': pacientes})

@login_required
def registro(request):
    return render(request, 'crear.html')

@login_required
def enviar(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    fecha= request.POST['fecha']
    sexo=request.POST["sexo"] 
    estado=request.POST["estado"] 
    tipo=request.POST['tipo']
    documento=request.POST['id']
    eps=request.POST['eps']
    tel=request.POST['telefono']
    dir=request.POST['direccion']
    email=request.POST['correo']
    alergia=request.POST['optradio']
    cirugia=request.POST['cirugia']
    vacuna=request.POST['vacuna']
    
    persona = {
        "documento" : documento,
        'nombre':  nombre,
        'apellido':  apellido,
        'fecha_nacimiento': fecha,
        'sexo':  sexo,
        'estado_civil':  estado,
        'tipo_documento':  tipo,
        'eps' : eps,
        'telefono' :  tel,
        'email' : email,
        'direccion': dir,
        'alergias':  alergia,
        'cirugias':  cirugia,
        'vacunas':  vacuna
    }
    print(persona)
    response = requests.post('http://127.0.0.1:8000/pacientes/api/paciente/', data = persona)
    messages.add_message(request=request,level= messages.SUCCESS, message="Paciente Registrado")
    return redirect('/pacientes')

@login_required
def historia(request, documento):
    
    
    response = requests.get('http://127.0.0.1:8000/pacientes/api/historia/')
    historia = response.json()
    response = requests.get(f'http://127.0.0.1:8000/pacientes/api/paciente/{documento}')
    paciente = response.json()
    
    historia_descripcion ={}
    list_diagnosticos=[]
    for x in historia:
        
        if x['paciente_id']== documento:
            
            id_historia = x['id']
            diagnostico= x['diagnostico']

            print(f'este es la lista de {diagnostico}')
            for d in diagnostico:
                print(f'items : {d}')
                response = requests.get(f'http://127.0.0.1:8000/pacientes/api/diagnostico/{d}')
                data=response.json()
                list_diagnosticos.append(data)
            
            
            print(list_diagnosticos)
            historia_descripcion= {
                "paciente": paciente,
                "id": id_historia,
                "diagnostico": list_diagnosticos,
            }
        else:
            diagnostico = ''
            
    return render(request, 'historia.html' , {'historia' : historia_descripcion})


def diagnostico(request):
    response = requests.get('https://sandbox-healthservice.priaid.ch/body/locations?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzMzY1NTg2LCJuYmYiOjE2NTMzNTgzODZ9.VU1YsqSZywcmX858Sqw_lPuIORuPTJ7Zft0UG4JmWTg&format=json&language=es-es')
    body = response.json()
    sintomas ={}
    if request.method == 'POST':
        sex =request.POST['sexo']
        part =request.POST['parte']
        print(part)
        response =requests.get(f'https://sandbox-healthservice.priaid.ch/symptoms/{part}/{sex}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzMzY1MDE4LCJuYmYiOjE2NTMzNTc4MTh9.20ZuYO7IcTtLlUciYW129IeP01wRBF9oDqUpBSI7EKU&format=json&language=es-es')
        sintomas =response.json()
        print(sintomas)
        
    return render(request, 'diagnostico.html', context={'body': body, 'sintomas': sintomas})