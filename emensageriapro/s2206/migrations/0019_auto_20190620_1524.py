# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2206', '0018_auto_20190620_1408'),
        ('controle_de_acesso', '0026_auto_20190620_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2206alvarajudicial',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206aprend',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206filiacaosindical',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206horario',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206horcontratual',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206infoceletista',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206infoestatutario',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206localtrabdom',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206localtrabgeral',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206observacoes',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206servpubl',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s2206trabtemp',
            name='excluido',
        ),
    ]