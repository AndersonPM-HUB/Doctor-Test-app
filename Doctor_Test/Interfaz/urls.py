from django.urls import  path, include
from . import views

urlpatterns =[
    path('', views.interfaz, name='interfaz'), 
    path('plataforma/', views.plataforma, name='plataforma'),
    path('pacientes/', views.pacientes, name='pacientes'), 
    path('registro/', views.registro, name='registro'), 
    path('enviar/', views.enviar, name='envio'),
    path('historia/<int:documento>/', views.historia, name='historia'),  
 
]