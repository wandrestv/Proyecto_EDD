from django import forms
from .models import Cargo, Departamento, Empleado

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese cargo',
                'class':'form-group',
                'required':True
            })
        }

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese departamento',
                'class':'form-group',
                'required':True
            })
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','cedula','cargo','departamento','sueldo','estado']
        widgets = {
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese nombre',
                'class':'form-group',
                'required':True
            }),
            'cedula':forms.TextInput(attrs={
                'placeholder':'Ingrese cedula',
                'class':'form-group',
                'required':True
            }),
            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese sueldo',
                'class':'form-group',
                'required':True
            })
        }