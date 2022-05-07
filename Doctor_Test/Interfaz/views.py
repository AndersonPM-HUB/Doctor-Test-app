from django.shortcuts import render

# Create your views here.
def interfaz(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def plataforma(request):
    return render(request, 'plataforma.html')