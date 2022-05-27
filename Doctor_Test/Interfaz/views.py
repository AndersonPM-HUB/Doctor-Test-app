
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
    
    #peticion de historia 
    response = requests.get('http://127.0.0.1:8000/pacientes/api/historia/')
    historia = response.json()
    #peticion de paciente
    response = requests.get(f'http://127.0.0.1:8000/pacientes/api/paciente/{documento}')
    paciente = response.json()
    #peticion de diagnosticos 
    response=requests.get(f'http://127.0.0.1:8000/pacientes/api/diagnostico/')
    diagnosticos = response.json()
    
    historia_descripcion ={}
    list_diagnosticos=[]
    
    for x in historia:
        if x['paciente_id']== documento:
            id_historia = x['id']
            print(id_historia)
            for y in diagnosticos:
                print(y)
                for i in y['id_historia']:
                    print(i)
                    if i == id_historia:
                        list_diagnosticos.append(y) 
                    print(list_diagnosticos)
                
                        
            historia_descripcion= {
                            "paciente": paciente,
                            "id": id_historia,
                            "diagnostico": list_diagnosticos,
                        }
             
    return render(request, 'historia.html' ,{'historia': historia_descripcion})

@login_required
def diagnostico(request):
    
    #mostrar partes del cuerpo 
    response = requests.get('https://sandbox-healthservice.priaid.ch/body/locations?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzNjY5NTQ0LCJuYmYiOjE2NTM2NjIzNDR9.iXR3SEEDEW4tjUXHdm5qLtBxFxF5iDjMahVoPQkNxK8&format=json&language=es-es')
    body = response.json()
    #mostrar sintomas
    response =requests.get(f'https://sandbox-healthservice.priaid.ch/symptoms?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzNjY5NTQ0LCJuYmYiOjE2NTM2NjIzNDR9.iXR3SEEDEW4tjUXHdm5qLtBxFxF5iDjMahVoPQkNxK8&format=json&language=es-es')
    sintomas =response.json()
    return render(request, 'diagnostico.html', context={'body': body, 'sintomas': sintomas})

@login_required
def resultados(request):
    
    if request.method == 'POST':
        #obtener sexo
        sex= request.POST['sexo'] 
        if sex == '0' or sex =='2':
            s='male'
        else:
            s ='female'
        
        #obtener edad
        age =request.POST['edad']
        year= 2022 - int(age)
        
        #obtener sintomas    
        sintoms = request.POST['sintoma']
        
        #generar diagnostico    
        response =requests.get(f'https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[{sintoms}]&gender={s}&year_of_birth={year}&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuZGVyc29ucGVkcm96YTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMDcyOSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMi0wNS0yMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjUzNjY5NTQ0LCJuYmYiOjE2NTM2NjIzNDR9.iXR3SEEDEW4tjUXHdm5qLtBxFxF5iDjMahVoPQkNxK8&format=json&language=es-es')
        
        if response.status_code == 200: 
            rta = response.json()
            
    return render(request, 'resultados.html', context={'rta':rta})

@login_required
def asignar(request):
    
    fecha =  request.POST['date']
    diagnostico = request.POST['contenido'] 
    tratamiento =  request.POST['tratamiento']  
    id= request.POST['id'] 
    
    data={
    
    "fecha":fecha,
    "descripcion": diagnostico,
    "tratamiento":tratamiento,
    "id_historia": [id]
    }
    
    response = requests.post('http://127.0.0.1:8000/pacientes/api/diagnostico/', data = data)
    messages.add_message(request=request,level= messages.SUCCESS, message="Diagnostico registrado")
    return redirect('/pacientes')

@login_required
def generar(request):
    cedula =  request.POST['cc']
    
    data={
        
        "paciente_id": cedula
    }
    response = requests.post('http://127.0.0.1:8000/pacientes/api/historia/', data = data)
    messages.add_message(request=request,level= messages.SUCCESS, message="Historial Creado")
    return redirect('/pacientes')
    