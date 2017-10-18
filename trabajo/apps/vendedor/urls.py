from django.conf.urls import url

from apps.inventario.views import index
urlpatterns = [
    url(r'^$', index ),
 ]
