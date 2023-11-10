from django import forms

class LimitCalculatorForm(forms.Form):
    x_value = forms.FloatField(label='Valor de x')
    function = forms.CharField(label='Función a evaluar')