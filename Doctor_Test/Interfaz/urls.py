from django.urls import  path
from . import views

urlpatterns =[
    path('', views.interfaz, name='interfaz'), 
    path('login/', views.login, name='login'),
]