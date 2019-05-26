# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2410', '0012_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2410homologtc',
            name='dthomol',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='nratolegal',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='tppenmorte',
            field=models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='cpfinst',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='dtinst',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='intaposentado',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
    ]
