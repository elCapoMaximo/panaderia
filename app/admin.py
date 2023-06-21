from django.contrib import admin
from .models import Usuario, Pan, biografia,registro

# Register your models here.
admin.site.register(Usuario)
admin.site.register(registro)
admin.site.register(Pan)
admin.site.register(biografia)