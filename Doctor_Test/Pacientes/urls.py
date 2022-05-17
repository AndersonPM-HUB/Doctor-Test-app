
from django.urls import  path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('paciente', views.Pacientes_api)
router.register('historia', views.Historia_api)
router.register('diagnostico', views.Diagnostico_api)

urlpatterns =[
    path('', include(router.urls)),

]
