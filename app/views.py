from django.shortcuts import render

# Create your views here.



def home (request):
    return render(request, 'app/index/index.html')

def login (request):
    return render(request, 'app/login/inicio_sesion.html')

def contacto (request):
    return render(request, 'app/contacto/index.html')

def carritocompra (request):
    return render(request, 'app/carritocompra/index.html')

def Registrarse (request):
    return render(request, 'app/Registrarse/registro.html')


def innovacion (request):
    return render(request, 'app/innovacion/inno.html')

def pedidos (request):
    return render(request, 'app/pedidos/pedidos.html')

def personalizacion (request):
    return render(request, 'app/personalizacion/personalizacion.html')


def seguimiento (request):
    return render



