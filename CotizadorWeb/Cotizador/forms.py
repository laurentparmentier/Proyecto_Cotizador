from django import forms
from django.forms import ModelForm, DateField

from django.forms.widgets import SelectDateWidget

from django.contrib.admin.widgets import AdminDateWidget

from .models import cotizacion, productos

from django.forms import formset_factory

class cotizacionForm(forms.ModelForm):

	fecha_cotizacion = DateField(widget=AdminDateWidget)
	class Meta:
		model = cotizacion
		fields = [
			'empresa',
			'usuario',
			'fecha_cotizacion',
			'cliente',
			'observaciones',
			]


class productosForm(forms.ModelForm):
	class Meta:
		model = productos
		fields = [
			'producto',
			'descripcion',
			'precio_unitario',
			'cantidad',
			'cotizacion',
 		]