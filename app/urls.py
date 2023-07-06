from django.urls import path
from .views import *

#Se linkean todas las paginas

urlpatterns = [
    path('base', base, name="base"),
    path('', home, name="home"),
    path('login/',login, name ="login" ),
    path('contacto/',contacto, name ="contacto" ),
    path('carritocompra/',carritocompra, name ="carritocompra" ),
    path('Registrarse/',Registrarse, name ="Registrarse" ),

    path('personalizacion/',personalizacion, name ="personalizacion" ),
    path('pedidos/',pedidos, name ="pedidos" ),
    path('innovacion/',innovacion, name ="innovacion" ),

    path ('agregar-producto/', agregar_producto, name="agregar_producto"),
    path ('listar-producto/', listar_producto, name="listar_producto"),
    path ('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path ('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    
    path('buscar/', buscar_producto, name='buscar_producto'),
    path('listar_buscar/', listar_buscar_producto, name='listar_buscar_producto'),
    
]

