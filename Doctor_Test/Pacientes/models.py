from django.db import models

# Create your models here.
class Paciente(models.Model): 
    documento = models.IntegerField(primary_key=True, null=False, unique=True)
    nombre= models.CharField(max_length=200)
    apellido= models.CharField(max_length=200)
    fecha_nacimiento= models.DateField()
    sexo= models.CharField(max_length=10)
    estado_civil= models.CharField(max_length=200)
    tipo_documento= models.CharField(max_length=200)
    eps= models.CharField(max_length=200)
    telefono= models.IntegerField()
    email =models.EmailField()
    direccion = models.CharField(max_length=200)
    alergias= models.BooleanField()
    cirugias= models.BooleanField()
    vacunas= models.BooleanField()
    

class diagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    fecha= models.DateField()
    descripcion=models.TextField()
    tratamiento=models.TextField()
    
    
class historia(models.Model):
    id = models.AutoField(primary_key=True)
    fecha=models.DateTimeField(auto_now_add=True)
    diagnostico = models.ManyToManyField(diagnostico)
    paciente_id= models.OneToOneField(Paciente, on_delete=models.CASCADE) #relacion de 1..1

