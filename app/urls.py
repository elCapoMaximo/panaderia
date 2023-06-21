from django.urls import path
from .views import *

#Se linkean todas las paginas

urlpatterns = [
    path('', home, name="home"),
    path('login/',login, name ="login" ),
    path('contacto/',contacto, name ="contacto" ),
    path('carritocompra/',carritocompra, name ="carritocompra" ),
    path('Registrarse/',Registrarse, name ="Registrarse" ),

    path('personalizacion/',personalizacion, name ="personalizacion" ),
    path('pedidos/',pedidos, name ="pedidos" ),
    path('innovacion/',innovacion, name ="innovacion" ),

]
