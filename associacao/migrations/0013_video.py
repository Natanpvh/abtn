# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associacao', '0012_auto_20170830_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_video', models.CharField(max_length=150)),
                ('url_video', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('0', 'Offline'), ('1', 'Online')], default='0', max_length=1)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Videos da Vila',
                'verbose_name': 'Video da Vila',
            },
        ),
    ]