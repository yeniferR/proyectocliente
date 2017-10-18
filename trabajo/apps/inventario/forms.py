from django import forms

from apps.inventario.models import Inventario


class InventarioForm(forms.ModelForm):

    class Meta:
        model=Inventario

        fields=[
            'nombre',
            'inicial',
            'ingreso',
            'final',
            'salida',
            'valor',
            'fecha',
            'persona',
            'producto',
        ]
        labels={
            'nombre':'nombre',
            'inicial':'inicial',
            'ingreso':'ingreso',
            'final':'final',
            'salida':'salida',
            'valor':'valor',
            'fecha':'fecha',
            'persona':'vendedor',
            'producto':'producto',

        }
        widgets={

            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'inicial': forms.TextInput(attrs={'class':'form-control'}),
            'ingreso': forms.TextInput(attrs={'class':'form-control'}),
            'final': forms.TextInput(attrs={'class':'form-control'}),
            'salida': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'producto': forms.CheckboxSelectMultiple(),

        }
