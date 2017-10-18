from django.shortcuts import render

from django.views.generic import TemplateView


class Inicio(TemplateView):
     template_name = 'inicio.html'

class Red(TemplateView):
     template_name = "red.html"

class Drive(TemplateView):
     template_name = "drive/drive.html"
