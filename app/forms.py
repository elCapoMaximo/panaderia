from django import forms
from .models import Pan
from django.contrib.auth.forms import UserCreationForm




class PanForm(forms.ModelForm):
    class Meta:
        model =Pan
        fields ='__all__'


        #SI LLEGA A TENER FECHA DE REGISTRO DEL PRODUCTO ES CON EL SIGUIENTE CODIGO 
        # widgets ={
        #     "fecha_registro":forms.SelectDateWidget()
        # }


class CustomUserCreationForm(UserCreationForm):
    pass