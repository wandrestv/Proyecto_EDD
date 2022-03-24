"""npago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Mantenimiento.views import inicio,crearCargo,listaCargo,editar_cargo,eliminar_cargo
from Mantenimiento.views import listaDepartamento,crearDepartamento,editar_departamento,eliminar_departamento
from Mantenimiento.views import listaEmpleado,crearEmpleado,editar_empleado,eliminar_empleado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,name="inicio"),

    path('lista_cargo/', listaCargo,name="lista_cargo"),
    path('crear_cargo/',crearCargo,name="crear_cargo"),
    path('editar_cargo/<int:codi>', editar_cargo,name="editar_cargo"),
    path('eliminar_cargo/<int:codi2>', eliminar_cargo,name="eliminar_cargo"),

    path('lista_departamento/', listaDepartamento,name="lista_departamento"),
    path('crear_departamento/',crearDepartamento,name="crear_departamento"),
    path('editar_departamento/<int:codi3>', editar_departamento,name="editar_departamento"),
    path('eliminar_departamento/<int:codi4>', eliminar_departamento,name="eliminar_departamento"),

    path('lista_empleado/', listaEmpleado,name="lista_empleado"),
    path('crear_empleado/',crearEmpleado,name="crear_empleado"),
    path('editar_empleado/<int:codi5>', editar_empleado,name="editar_empleado"),
    path('eliminar_empleado/<int:codi6>', eliminar_empleado,name="eliminar_empleado"),
]
