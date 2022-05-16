from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    return redirect('/pacientes')

@login_required
def historia(request, documento):
    response = requests.get('http://127.0.0.1:8000/pacientes/api/historia/')
    diagnostico = response.json()
    response = requests.get(f'http://127.0.0.1:8000/pacientes/api/paciente/{documento}')
    paciente = response.json()
    historia ={}
    for x in diagnostico:
        
        if x['paciente_id']== documento:
            diagnostico= x['diagnostico']
            id= x['id']
            fecha = x['fecha']
            historia= {
                "paciente": paciente,
                "id": id,
                "fecha": fecha,
                "diagnostico": diagnostico,
            }
            print(historia)
        else:
            diagnostico = ''
            
        
    
    return render(request, 'historia.html' , {'historia' : historia})