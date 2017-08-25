from django.db import models

# Create your models here.
class RRHH(models.Model):
    sex= (
    ('M', 'Male'),
    ('F','Female'),
    )

    name=models.CharField(max_length=50,help_text="Ingrese su Nombre: ")
    telphone=models.CharField(max_length=10, help_text="Ingrese su numero telefonico: ")
    sex=models.CharField(max_length=1, help_text="Seleccione su genero: ")
    bday=models.DateField()
