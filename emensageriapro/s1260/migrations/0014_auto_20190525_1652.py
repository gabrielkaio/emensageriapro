# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1260', '0013_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='nrinsc',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], null=True),
        ),
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='vrcomerc',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='codsusp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='nrproc',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='s1260infoprocjud',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='dtemisnf',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='nrdocto',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1260nfs',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1260tpcomerc',
            name='indcomerc',
            field=models.IntegerField(choices=[(2, '2 - Comercializa\xe7\xe3o da Produ\xe7\xe3o efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa f\xedsica por Produtor Rural Pessoa F\xedsica, inclusive por Segurado Especial ou por Pessoa F\xedsica n\xe3o produtor rural'), (3, '3 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PF/Seg. Especial - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA) ou a Intermedi\xe1rio PF'), (7, '7 - Comercializa\xe7\xe3o da Produ\xe7\xe3o Isenta de acordo com a Lei n\xb0 13.606/2018'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o da Pessoa F\xedsica/Segurado Especial para Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o da Produ\xe7\xe3o no Mercado Externo.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1260tpcomerc',
            name='vrtotcom',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]