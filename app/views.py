from django.shortcuts import render, redirect, get_object_or_404
#from .models import Producto
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


def base (request):
    return render(request, 'app/base/base.html')
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

def agregar_producto(request):

    data ={
''      'form':PanForm()

    }
    if request.method =='POST':
        formulario = PanForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Pan Registrado")

        else:
            data["form"]= formulario

    return render(request, 'app/crud/agregar.html',data)


def listar_producto(request):

    cproductos = Pan.objects.all()
    data ={
        'pan':cproductos
        
    }

 
    return render(request, 'app/crud/listar.html',data)



def modificar_producto(request, id):

 
        mproducto = get_object_or_404(Pan, codigo=id)

        data = {
                'form': PanForm(instance=mproducto)

            }

        if request.method =='POST':
            formulario = PanForm(data=request.POST, instance=mproducto, files =request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request,"Modificado Correctamente")
                return redirect(to="listar_producto")
            data['form'] = formulario


 
        return render(request, 'app/crud/modificar.html',data)


def eliminar_producto(request,id):
    eproducto = get_object_or_404(Pan, codigo=id)
    eproducto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to="listar_producto")

def modelo_json(request):
    data = list(Pan.objects.values('nombre', 'precio', 'imagen'))
    return JsonResponse(data, safe=False)
