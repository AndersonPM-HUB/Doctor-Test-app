
from django.urls import  path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('paciente', views.PacienteView)

urlpatterns =[
    # path('', views.inicio, name = 'inicio'),
    # path('registro/', views.registro, name = 'registro'),
    # path('actualizar/<int:documento>', views.actualizar, name = 'actualizar'),
    # path('eliminar/<int:documento>', views.eliminar, name = 'eliminar'),
    # path('registro/enviar/', views.enviar, name = 'enviar'),
    path('api/', include(router.urls)),

]
