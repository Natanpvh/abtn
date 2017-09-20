# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Preenchido automaticamente, não editar.', max_length=255, unique=True, verbose_name='Slug / URL'),
        ),
    ]