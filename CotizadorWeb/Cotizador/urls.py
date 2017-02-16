from django.conf.urls import url

from .views import (
    index,
    nueva_cotizacion,
    nuevo_producto,
    consultar_cotizacion,
    listar_cotizacion,
    #eliminar_cotizacion,
    )

# from .printing import(
#     generador_pdf,
#     )
app_name = 'Cotizador'

urlpatterns = [
    url(r'^$', index),
    url(r'^nueva/$', nueva_cotizacion),
    url(r'^productos/$', nuevo_producto),
    url(r'^consulta/(?P<id>\d+)/$', consultar_cotizacion),
    url(r'^lista/$', listar_cotizacion),
    #url(r'^eliminar/$', eliminar_cotizacion),
    #url(r'^pdf/$', generador_pdf),

]