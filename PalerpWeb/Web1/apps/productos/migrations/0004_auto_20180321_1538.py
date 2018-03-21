# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-21 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cadenaCaracteristicas',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='producto',
            name='codigofabricante',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='producto',
            name='minicodigo',
            field=models.CharField(default='', max_length=10),
        ),
    ]