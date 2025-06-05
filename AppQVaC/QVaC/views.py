from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index (request):
    return render (request,"index.html")

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
            return render(request, 'busqueda_recetas.html')  
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def registro(request):
    if request.method == 'GET':
        return render(request,'registro.html') #Esto muestra la página login como HTML porque el método POST de la función registro maneja una API que responde a un POST con JSON (para autenticación). Recordar que el profe renderiza paginas con formularios que los pasa como diccionarios.
    
    elif request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        password = request.POST.get ('contraseña')
        confirmar_password = request.POST.get('confirmarcontraseña')

        # Validación básica
        if not all([nombre, apellido, correo, password, confirmar_password]):
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'registro.html')

        if password != confirmar_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'registro.html')

        if User.objects.filter(username=correo).exists():
            messages.error(request, "El correo ya está registrado.")
            return render(request, 'registro.html')

        # Crear el usuario
        user = User.objects.create_user(
            username=correo,
            email=correo,
            password=password
        )
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        
        """
        first_name y last_name no se aceptan directamente en create_user() ==> Aunque el modelo User tiene campos como first_name y last_name, la función create_user() no los maneja directamente.
         
        La función que los maneja directamente es User(...) pero perdemos las validaciones automáticas del password.

        Entonces preferimos usar create_user() porque:
        1. internamente llama a set_password() para encriptar la contraseña.
        2. Se asegura de que el usuario quede guardado correctamente con los mínimos requeridos.
        3. Después podemos modificar los campos adicionales como cualquier otro objeto Python/Django, así:
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            Esto te permite mantener la validación automática del usuario y asegurar que los datos extra (como el nombre) también queden guardados.
        
        """
        messages.success(request, "Usuario registrado exitosamente. Ahora puedes iniciar sesión.")
        return redirect('login')
