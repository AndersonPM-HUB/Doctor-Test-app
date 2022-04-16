
from django.urls import  path
from . import views



urlpatterns =[
    path('', views.inicio, name = 'inicio'),
    path('registro/', views.registro, name = 'registro'),
    path('actualizar/', views.actualizar, name = 'actualizar'),
    path('eliminar/', views.eliminar, name = 'eliminar'),
]