# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1030', '0005_auto_20181213_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1030alteracao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1030alteracaonovavalidade',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1030exclusao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1030inclusao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]