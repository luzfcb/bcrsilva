# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20180205_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemnota',
            name='id',
        ),
        migrations.AddField(
            model_name='itemnota',
            name='nota',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE,
                                       primary_key=True, serialize=False, to='estoque.Nota'),
            preserve_default=False,
        ),
    ]
