# -*- coding: utf-8-*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.shortcuts import render


from .models import cotizacion, productos
from .forms import cotizacionForm, productosForm
from django.contrib import auth
#from django.contrib.auth.decorators import login_required
#from django.forms import modelformset_factory


# Create your views here.

#@login_required(login_url='/accounts/user_login/')
def index(request):
  return render(request, 'index.html')
  # queryset = cotizacion.objects.filter(usuario=int(request.user.id))[:6]
  # context = {'titulo': 'Tus últimas cotizaciones:',
  #            'lista_objetos':queryset}
  #return render(request, 'index.html',context)


# @login_required(login_url='/accounts/user_login/')
def nueva_cotizacion(request):
#  return render(request, 'formulario_cotizacion.html')
   form = cotizacionForm(request.POST or None)
   if form.is_valid():
     iva = 0
     subtotal = 0
     total = 0
     instance = form.save(commit=False)
     instance.save()
     return redirect('Cotizador.views.nuevo_producto')
              
   context = {'titulo' : 'Nueva Cotización',
             'form':form,}
   return render(request, 'formulario_cotizacion.html', context)

    
  
# @login_required(login_url='/accounts/user_login/')
def nuevo_producto(request):
  form = productosForm(request.POST or None)
  productoFormSet = formset_factory(productosForm)
  formset = productoFormSet(request.POST or None)
  
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()

  context = {'titulo': 'Registro de Productos',
            'formset':formset,
            }
  return render(request, 'formulario_producto.html', context)

# @login_required(login_url='/accounts/user_login/')
def consultar_cotizacion(request, id = None):                       #retrieve/read
  instance = get_object_or_404(cotizacion, id=id)
  queryset = productos.objects.filter(cotizacion_id = id)
  context = {'titulo' : 'Cotizacion '+id,
            'instance': instance,
            'lista_productos': queryset}
  return render(request, 'consulta.html', context)

# @login_required(login_url='/accounts/user_login/')
def listar_cotizacion(request):
  queryset = cotizacion.objects.all().order_by('-fecha_de_creacion')
  context = {
    'lista_objetos' : queryset,
    'titulo' : 'Cotizaciones Anteriores'}
  return render(request, 'consulta_lista.html', context)

# @login_required(login_url='/accounts/user_login/')
# def eliminar_cotizacion(request):
#   context = {'titulo' : 'Eliminar Cotizacion'}
#   return render(request, 'template1.html', context)