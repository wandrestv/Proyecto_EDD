from logging import exception
from django.shortcuts import redirect, render,HttpResponse
from .models import Cargo, Departamento, Empleado
from .forms import CargoForm,DepartamentoForm,EmpleadoForm

# Create your views here.

#Vista de Inicio
def inicio(request):
    return render(request,"inicio.html")

#Vista de cargos

def listaCargo(request):
    cargo_form = CargoForm(request.POST)
    cargos = Cargo.objects.all()
    return render(request, "pages/lista_cargo.html",{'cargoForm': cargo_form, 'cargos':cargos})

def crearCargo(request):
    if request.method == "POST":
        cargo_form = CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('lista_cargo')
    else:
        print("entro por get")
    cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/crear_cargo.html", {'cargoForm': cargo_form, 'cargos':cargos ,'accion':'Crear'})

def editar_cargo(request,codi):
    error,cargo_form=None,None
    try:
        cargo = Cargo.objects.get(id=codi)
        if request.method == "GET":
            cargo_form = CargoForm(instance=cargo)
        else:
            cargo_form = CargoForm(request.POST,instance=cargo)
            if cargo_form.is_valid():
                cargo_form.save()
                return redirect('lista_cargo')

    except exception as e:
        error=e
    cargos = Cargo.objects.all()
    return render(request, "pages/editar_cargo.html", {'cargoForm': cargo_form, 'cargos':cargos ,'accion':'Actualizar'})

def eliminar_cargo(request,codi2):
    cargo = Cargo.objects.get(id=codi2)
    if request.method == 'POST':
        cargo.delete()
        return redirect('lista_cargo')
    return render(request, "pages/eliminar_cargo.html", {'cargo':cargo})

#Vista de Departamentos

def listaDepartamento(request):
    depa_form = DepartamentoForm(request.POST)
    departamentos = Departamento.objects.all()
    return render(request, "pages/lista_departamento.html",{'depaForm': depa_form, 'departamentos':departamentos})

def crearDepartamento(request):
    if request.method == "POST":
        depa_form = DepartamentoForm(request.POST)
        if depa_form.is_valid():
            depa_form.save()
            return redirect('lista_departamento')
    else:
        print("entro por get")
    depa_form = DepartamentoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/crear_departamento.html", {'depaForm': depa_form, 'departamentos':departamentos ,'accion':'Crear'})

def editar_departamento(request,codi3):
    error,depa_form=None,None
    try:
        departamento = Departamento.objects.get(id=codi3)
        if request.method == "GET":
            depa_form = DepartamentoForm(instance=departamento)
        else:
            depa_form = CargoForm(request.POST,instance=departamento)
            if depa_form.is_valid():
                depa_form.save()
                return redirect('lista_departamento')

    except exception as e:
        error=e
    departamentos = Departamento.objects.all()
    return render(request, "pages/editar_departamento.html", {'depaForm': depa_form, 'departamentos': departamentos ,'accion':'Actualizar'})

def eliminar_departamento(request,codi4):
    departamento = Departamento.objects.get(id=codi4)
    if request.method == 'POST':
        departamento.delete()
        return redirect('lista_departamento')
    return render(request, "pages/eliminar_departamento.html", {'departamento':departamento})

#Vista de Empleados

def listaEmpleado(request):
    emple_form = EmpleadoForm(request.POST)
    empleados = Empleado.objects.all()
    return render(request, "pages/lista_empleado.html",{'empleForm': emple_form, 'empleados':empleados})

def crearEmpleado(request):
    if request.method == "POST":
        emple_form = EmpleadoForm(request.POST)
        if emple_form.is_valid():
            emple_form.save()
            return redirect('lista_empleado')
    else:
        print("entro por get")
    emple_form = EmpleadoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/crear_empleado.html", {'empleForm': emple_form, 'empleados':empleados ,'accion':'Crear'})

def editar_empleado(request,codi5):
    error,emple_form=None,None
    try:
        empleado = Empleado.objects.get(id=codi5)
        if request.method == "GET":
            emple_form = EmpleadoForm(instance=empleado)
        else:
            emple_form = EmpleadoForm(request.POST,instance=empleado)
            if emple_form.is_valid():
                emple_form.save()
                return redirect('lista_empleado')

    except exception as e:
        error=e
    empleados = Empleado.objects.all()
    return render(request, "pages/editar_empleado.html", {'empleForm': emple_form, 'empleados': empleados ,'accion':'Actualizar'})

def eliminar_empleado(request,codi6):
    empleado = Empleado.objects.get(id=codi6)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleado')
    return render(request, "pages/eliminar_empleado.html", {'empleado':empleado})