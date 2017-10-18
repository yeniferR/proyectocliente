from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from apps.inventario.forms import InventarioForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from apps.inventario.forms import InventarioForm
from apps.inventario.models import Inventario


def index(request):
    return render(request,'inventario/index.html')

def inventario_view(request):
    if request.method=='POST':
        form= InventarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inventario:index')
    else:
        form=InventarioForm()

    return render(request,'inventario/inventario_form.html',{'form':form})

class InventarioCreate(CreateView):
	model = Inventario
	form_class = InventarioForm
	template_name = 'inventario/inventario_form.html'
	success_url = reverse_lazy('inventario:index')
