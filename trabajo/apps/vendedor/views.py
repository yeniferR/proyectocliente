from django.shortcuts import render
from django.http import HttpResponse


def index_vendedor(request):
    return HttpResponse("vendedor del año jjaja")
# Create your views here.
