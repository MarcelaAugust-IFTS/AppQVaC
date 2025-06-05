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

@csrf_exempt  # Úsalo si no estás manejando el CSRF token desde el frontend aún
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('usuario')
        password = data.get('contraseña')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'mensaje': 'Autenticado correctamente'})
        else:
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=401)

    return JsonResponse({'error': 'Método no permitido'}, status=405)