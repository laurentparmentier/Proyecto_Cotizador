from __future__ import unicode_literals

from django.db import models
from django.contrib import auth

# Create your models here.

class cotizacion(models.Model):
   	CHOICES = (('CAD','CAD SPORT'),('ORA','ORANGE SPORT'),('GOL','GOLDEP'))
   	empresa = models.CharField(max_length=3, choices=CHOICES)
   	usuario = models.ForeignKey('auth.User')
   	cliente = models.CharField(max_length=120)
   	fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)
   	fecha_de_modificacion = models.DateTimeField(auto_now=True, auto_now_add=False)
   	fecha_cotizacion = models.DateField()
   	observaciones = models.TextField(default='Precios sujetos a cambios sin previo aviso.')
   	iva = models.DecimalField(max_digits=20, decimal_places=4, default=0)
   	subtotal = models.DecimalField(max_digits=20, decimal_places=4, default=0)
   	total = models.DecimalField(max_digits=20, decimal_places=4, default=0)
   	#def __unicode__(self):
    #	return self.cliente

   	#def get_absolute_url(self):
   	#	return '/cotizador/consulta/%s/' %(self.id)

class productos(models.Model):
	producto = models.CharField(max_length=120)
   	descripcion = models.CharField(max_length=240)
  	precio_unitario = models.DecimalField(max_digits=12, decimal_places=4, default=0)
   	cantidad = models.IntegerField(default=1)
   	cotizacion = models.ForeignKey('cotizacion', on_delete=models.CASCADE)