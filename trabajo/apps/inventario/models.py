from django.db import models

# Create your models here.

from apps.vendedor.models import Persona

class Producto(models.Model):
      nombre=models.CharField(max_length=50)

      def __str__ (self):
          return '{}'.format (self.nombre)



class Inventario(models.Model):
    nombre=models.CharField(max_length=50)
    inicial=models.IntegerField()
    ingreso=models.IntegerField()
    final=models.IntegerField()
    salida=models.IntegerField()
    valor=models.IntegerField()
    fecha=models.DateField()
    persona= models.ForeignKey(Persona, null=True, blank= True, on_delete=models.CASCADE)
    producto=models.ManyToManyField(Producto, blank=True)
