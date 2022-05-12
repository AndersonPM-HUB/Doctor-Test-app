from django.urls import  path, include
from . import views

urlpatterns =[
    path('', views.interfaz, name='interfaz'), 
    path('plataforma/', views.plataforma, name='plataforma'),
    path('pacientes/', views.pacientes, name='pacientes'), 
    
 
]