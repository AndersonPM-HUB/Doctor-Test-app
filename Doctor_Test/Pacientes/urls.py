
from django.urls import  path
from . import views



urlpatterns =[
    path('', views.inicio, name = 'inicio'),
    path('registro/', views.registro, name = 'registro'),
    path('actualizar/<int:documento>', views.actualizar, name = 'actualizar'),
    path('eliminar/<int:documento>', views.eliminar, name = 'eliminar'),
    path('registro/enviar/', views.enviar, name = 'enviar'),
]
