from django.contrib import admin
from .models import Pan


class PanAdmin(admin.ModelAdmin):
    list_display  =  ["codigo","nombre","precio"]   #MUESTRA LOS CAMPOS QUE QUIERA
    list_editable =  ["precio"]                     #EDITA EL PRECIO
    search_fields =  ["nombre"]                     #Para filtrar
    list_filter   =  ["precio"]                     #Filtrar por precio



admin.site.register(Pan,PanAdmin)

