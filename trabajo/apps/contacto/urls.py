from django.conf.urls import url, include
from apps.contacto.views import contacto

urlpatterns = [
    url(r'^$', contacto,name='contacto'),
]
