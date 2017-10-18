from django.conf.urls import url, include
from apps.inventario.views import index, inventario_view,InventarioCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevo$',InventarioCreate.as_view(),name='inventario_crear'),
]
