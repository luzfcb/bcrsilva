# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0006_auto_20180206_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemnota',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=7, verbose_name='Valor'),
            preserve_default=False,
        ),
    ]