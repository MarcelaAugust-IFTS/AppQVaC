"""
URL configuration for AppQVaC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from QVaC import views #de la carpeta QVaC importa las vistas (esta carpeta se crea cuando se inicializa la app)

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta al panel de administración de Django
    path("", views.index, name = "index"), # Agrego la ruta del index (se pone solo comillas) y defino la función index que estará en el archivo views.py
    path("login/", views.vista_login, name="login"), # Ruta para la vista de login
    path("registro/", views.registro, name = "registro") #Ruta para la vista de registro
]
