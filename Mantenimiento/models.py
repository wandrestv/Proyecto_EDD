from tabnanny import verbose
from django.db import models

# Create your models here.

class Cargo(models.Model):
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False,auto_now=True)
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['descripcion']
    def __str__(self):
        return self.descripcion
 
class Departamento(models.Model):
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False,auto_now=True)
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['descripcion']
    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,blank=False,null=True)
    cedula = models.IntegerField(blank=False,null=True)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=7,decimal_places=2)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False,auto_now=True)
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['nombre']
    def __str__(self):
        return self.nombre