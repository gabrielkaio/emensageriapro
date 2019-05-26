# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1260', '0009_auto_20190204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=15),
        ),
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='s1260_tpcomerc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1260ideadquir_s1260_tpcomerc', to='s1260.s1260tpComerc'),
        ),
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')], default=0),
        ),
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='vrcomerc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='codsusp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='nrproc',
            field=models.CharField(default=b'A', max_length=21),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='s1260_tpcomerc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1260infoprocjud_s1260_tpcomerc', to='s1260.s1260tpComerc'),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')], default=0),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='dtemisnf',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='nrdocto',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='s1260_ideadquir',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1260nfs_s1260_ideadquir', to='s1260.s1260ideAdquir'),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1260tpcomerc',
            name='indcomerc',
            field=models.IntegerField(choices=[(2, '2 - Comercializa\xe7\xe3o da Produ\xe7\xe3o efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa f\xedsica por Produtor Rural Pessoa F\xedsica, inclusive por Segurado Especial ou por Pessoa F\xedsica n\xe3o produtor rural'), (3, '3 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PF/Seg. Especia - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA) ou a Intermedi\xe1rio PF'), (7, '7 - Comercializa\xe7\xe3o da Produ\xe7\xe3o Isenta de acordo com a Lei no 13.606/2018'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o da Pessoa F\xedsica/Segurado Especial para Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o da Produ\xe7\xe3o no Mercado Externo')], default=0),
        ),
        migrations.AlterField(
            model_name='s1260tpcomerc',
            name='s1260_evtcomprod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1260tpcomerc_s1260_evtcomprod', to='esocial.s1260evtComProd'),
        ),
        migrations.AlterField(
            model_name='s1260tpcomerc',
            name='vrtotcom',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
    ]
