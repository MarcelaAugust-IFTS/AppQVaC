from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

# Create your views here.

def index (request):
    return render (request,"index.html")

#def login (request):
#    return render (request,"login.html")

'''def login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la vista 'home' después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')  # Asegúrate de que el archivo se llame login.html'''

#No usar login porque es una función definida en Django (la importamos con django.contrib.auth.login)
def vista_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')  #Esto muestra la página login como HTML porque el método POST de la función login maneja una API que responde a un POST con JSON (para autenticación). Recordar que el profe renderiza paginas con formularios que los pasa como diccionarios.

    elif request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')  
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)