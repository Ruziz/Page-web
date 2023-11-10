from django.contrib.auth.forms import UserCreationForm
from django import forms
#registro

class creacionUser(UserCreationForm):
    pass 

class LimitCalculatorForm(forms.Form):
    x_value = forms.FloatField(label='Valor de x')
    function = forms.CharField(label='Función a evaluar')