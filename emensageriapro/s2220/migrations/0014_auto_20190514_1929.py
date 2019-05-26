# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2220', '0013_auto_20190513_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2220exame',
            name='dtexm',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='dtinimonit',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='interprexm',
            field=models.IntegerField(choices=[(1, '1 - EE'), (2, '2 - SC'), (3, '3 - SC+.')]),
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='ordexame',
            field=models.IntegerField(choices=[(1, '1 - Inicial'), (2, '2 - Sequencial.')]),
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='procrealizado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='s2220_evtmonit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2220exame_s2220_evtmonit', to='esocial.s2220evtMonit'),
        ),
    ]
