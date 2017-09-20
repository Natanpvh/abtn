# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Categoria:')),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('texto', tinymce.models.HTMLField()),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('status', models.CharField(choices=[('0', 'Offiline'), ('1', 'Online')], default='0', max_length=1)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='associacao.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'verbose_name': 'Post',
            },
        ),
    ]