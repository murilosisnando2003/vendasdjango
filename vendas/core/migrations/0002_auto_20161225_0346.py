# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-25 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço'),
        ),
    ]
