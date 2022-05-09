from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def interfaz(request):
    return render(request, 'index.html')


@login_required
def plataforma(request):
    return render(request, 'plataforma.html')