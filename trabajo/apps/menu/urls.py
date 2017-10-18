from django.conf.urls import url, include
from apps.menu.views import menu

urlpatterns = [
    url(r'^$', menu,name='menu'),
]
