from django.conf.urls import  include, url
from .views import Inicio, Red,Drive
from django.contrib.auth.decorators import login_required


urlpatterns = [
  url(r'^inicio/$',Inicio.as_view(),name='facebook'),
  url(r'^red/$', Red.as_view(), name="red"),
  url(r'^drive/$', Drive.as_view(), name="drive"),
]
