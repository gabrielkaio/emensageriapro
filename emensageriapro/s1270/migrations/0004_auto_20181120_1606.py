# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1270', '0003_auto_20181119_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='codlotacao',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='s1270_evtcontratavnp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1270remunavnp_s1270_evtcontratavnp', to='esocial.s1270evtContratAvNP'),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrbccp00',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrbccp13',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrbccp15',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrbccp20',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrbccp25',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrbcfgts',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='vrdesccp',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
    ]
