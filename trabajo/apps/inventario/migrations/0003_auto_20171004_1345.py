# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 18:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20171004_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='Fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='InventarioFinal',
            new_name='final',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='InventarioInicial',
            new_name='inicial',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='Persona',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='Producto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='Salida',
            new_name='salida',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='Valor',
            new_name='valor',
        ),
    ]
