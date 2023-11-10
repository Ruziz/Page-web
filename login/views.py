from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from .forms import creacionUser, LimitCalculatorForm
import sympy
@login_required
def home(request):
    return render(request=request,template_name="home.html")

def exit(request):
    logout(request)
    return redirect("home")

def registro(request):
    data={
        'form': creacionUser()
    }
    if request.method == 'POST':
        formulario = creacionUser(data= request.POST)
        if formulario.is_valid():
            user= formulario.save()
            login(request,user)
            return redirect("home")
        data['form']=formulario    
    return render(request, 'registration/registro.html', data)
def limites(request):
    result_data = None

    if request.method == 'POST':
        form = LimitCalculatorForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x_value']
            function_expression = form.cleaned_data['function']

            try:
                # Intenta evaluar la función ingresada por el usuario
                f = sympy.sympify(function_expression)
                fx = f.subs('x', x)
                result_data = [(x, fx)]
            except (ValueError, sympy.SympifyError):
                # Maneja errores si la función no es válida
                result_data = [('Error', 'Función no válida')]

    else:
        form = LimitCalculatorForm()

    return render(request, 'limites.html', {'form': form, 'result_data': result_data})
def derivadas(request):
    return render(request,"derivadas.html")
def simplificacion(request):
    return render(request,"simplificacion.html")