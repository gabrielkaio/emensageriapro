# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2231', '0005_auto_20190202_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2231fimcessao',
            options={'managed': True, 'ordering': ['s2231_evtcessao', 'dttermcessao'], 'permissions': (('can_view_s2231_fimcessao', 'Can view s2231_fimcessao'),)},
        ),
        migrations.AlterModelOptions(
            name='s2231inicessao',
            options={'managed': True, 'ordering': ['s2231_evtcessao', 'dtinicessao', 'cnpjcess', 'infonus', 'indcessao'], 'permissions': (('can_view_s2231_inicessao', 'Can view s2231_inicessao'),)},
        ),
    ]