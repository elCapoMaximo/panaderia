from django.shortcuts import render, redirect, get_object_or_404
#from .models import Producto
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Pan
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
    
    productos = Pan.objects.all()
    data ={
        'pan':productos
        
    }
    
    return render(request, 'app/carritocompra/index.html',data)

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

@permission_required('app.add_pan')
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

@permission_required('app.view_pan')
def listar_producto(request):

    productos = Pan.objects.all()
    data ={
        'pan':productos
        
    }
    return render(request, 'app/crud/listar.html',data)

from django.http import HttpResponseRedirect

def modificar_producto(request, id):
    mproducto = get_object_or_404(Pan, codigo=id)
    data = {
        'form': PanForm(instance=mproducto)
    }

    if request.method == 'POST':
        formulario = PanForm(data=request.POST, instance=mproducto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            if 'previous_url' in request.session:
                previous_url = request.session['previous_url']
                del request.session['previous_url']
                return HttpResponseRedirect(previous_url)
            else:
                return redirect('listar_producto')
        data['form'] = formulario
    else:
        request.session['previous_url'] = request.META.get('HTTP_REFERER')

    return render(request, 'app/crud/modificar.html', data)

def eliminar_producto(request, id):
    eproducto = get_object_or_404(Pan, codigo=id)
    url_anterior = request.META.get('HTTP_REFERER')
    eproducto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(url_anterior)

def modelo_json(request):
    data = list(Pan.objects.values('nombre', 'precio', 'imagen'))
    return JsonResponse(data, safe=False)

def buscar_producto(request):
    query = request.GET.get('query')
    
    if query:
        productos = Pan.objects.filter(nombre__iexact=query)
    else:
        productos = Pan.objects.all()
        data ={
            'pan':productos
            }
        
    
    return render(request, 'app/carritocompra/index.html', {'productos': productos, 'query': query})

def buscar(request):
    return render(request, 'app/buscar/buscar.html')


def listar_buscar_producto(request):
    query = request.GET.get('query')
    
    if query:
        productos = Pan.objects.filter(nombre__iexact=query)
    else:
        productos = Pan.objects.all()
        data ={
            'pan':productos
            }
        
    
    return render(request, 'app/crud/listar.html', {'productos': productos, 'query': query})
