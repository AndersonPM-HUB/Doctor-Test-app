from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente



# Create your views here.
def inicio(request):
    #obtiene la info a partir del modelo 
    pacientes = Paciente.objects.all()
    print(pacientes)
    return render (request, 'Index.html', {'pacientes': pacientes})

def registro(request):
    return render (request, 'crear.html')

def actualizar(request,documento):
    paciente = Paciente.objects.get(documento=documento)
    return render (request, 'editar.html')

def eliminar(request,documento):
    paciente = Paciente.objects.get(documento=documento)
    paciente.delete()
    return redirect ('/pacientes')



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
    
    persona = Paciente.objects.create(
        documento = documento,
        nombre= nombre,
        apellido= apellido,
        fecha_nacimiento= fecha,
        sexo= sexo,
        estado_civil= estado,
        tipo_documento= tipo,
        eps= eps,
        telefono= tel,
        email =email,
        direccion = dir,
        alergias= alergia,
        cirugias= cirugia,
        vacunas= vacuna
    )
    
    print(persona)

    return redirect('/pacientes')
    
    