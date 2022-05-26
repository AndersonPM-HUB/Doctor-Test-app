from tkinter import S
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests

gender =''
anio = ''
s =''
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
    response = requests.get('https://sandbox-healthservice.priaid.ch/body/locations?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzNTQzNTY0LCJuYmYiOjE2NTM1MzYzNjR9.3HOCK0U29soFKHHsmYtW67Cb18Aym8wTCWvw21aBMeM&format=json&language=es-es')
    body = response.json()
    sintomas ={}
    
    if request.method == 'POST':
        if 'sexo' in request.POST:
            sex= request.POST['sexo']
            gender = sex
        else:
            sex = gender
        
        
        if 'parte'in request.POST:
            part =request.POST['parte']
        else :
            part = None
            
        response =requests.get(f'https://sandbox-healthservice.priaid.ch/symptoms/{part}/{sex}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzNTQzNzA4LCJuYmYiOjE2NTM1MzY1MDh9.u6_3bS8eo1QSQVvuKRVN1InJ5LmuyGytglEdaTI0ZEk&format=json&language=es-es')
        if response.status_code == 200:
            sintomas =response.json()
        
        if 'edad'in request.POST:
            age =request.POST['edad']
            year= 2022 - int(age)
            anio = year
        
        
        if gender == '0' or gender =='2':
            s='male'
        else:
            s ='female'
        
        
        
    return render(request, 'diagnostico.html', context={'body': body, 'sintomas': sintomas})

def resultados(request):
    
    if request.method == 'POST':
        lista= request.POST['sintoma']
             
        print(s)
        print(anio)
        print(lista)
        response = requests.get(f'https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[{lista}]&gender={s}&year_of_birth={anio}&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzNTQ2MzU4LCJuYmYiOjE2NTM1MzkxNTh9.V8StQmzPtS7spyIIqPhAXfHhm-88cLs0Ac4QxIQ1T7k&format=json&language=es-es')
        diag =response.json()
        print(diag)
    
    return render(request, 'resultados.html')
    