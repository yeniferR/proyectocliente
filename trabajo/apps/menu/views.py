from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def menu(request):
    return render(request,'menu/menu.html')
