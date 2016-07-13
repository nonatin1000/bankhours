# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20160711_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='work_regime',
            field=models.IntegerField(blank=True, choices=[(40, 'Horas'), (30, 'Horas'), (20, 'Horas')], default=40, help_text='*', null=True, verbose_name='Regime de Trabalho'),
        ),
    ]
