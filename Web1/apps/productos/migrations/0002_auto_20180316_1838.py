# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-16 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
