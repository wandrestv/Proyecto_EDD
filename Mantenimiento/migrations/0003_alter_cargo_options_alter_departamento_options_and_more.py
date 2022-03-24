# Generated by Django 4.0.3 on 2022-03-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mantenimiento', '0002_cargo_descripcion_cargo_estado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['descripcion'], 'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['descripcion'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantenimiento.cargo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mantenimiento.departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['nombre'],
            },
        ),
    ]
