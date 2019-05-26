# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2306', '0013_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='cep',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='cnpjagntinteg',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='dsclograd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='nmrazao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='nrlograd',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2306cargofuncao',
            name='codcargo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='dtprevterm',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='natestagio',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o Obrigat\xf3rio.'), (b'O', 'O - Obrigat\xf3rio')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='nivestagio',
            field=models.IntegerField(choices=[(1, '1 - Fundamental'), (2, '2 - M\xe9dio'), (3, '3 - Forma\xe7\xe3o Profissional'), (4, '4 - Superior'), (8, '8 - Especial'), (9, '9 - M\xe3e social. (Lei 7644, de 1987).')], null=True),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='nmrazao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2306infotrabcedido',
            name='indremuncargo',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o. Valores v\xe1lidos: S, N.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2306remuneracao',
            name='undsalfixo',
            field=models.IntegerField(choices=[(1, '1 - Por Hora'), (2, '2 - Por Dia'), (3, '3 - Por Semana'), (4, '4 - Por Quinzena'), (5, '5 - Por M\xeas'), (6, '6 - Por Tarefa'), (7, '7 - N\xe3o aplic\xe1vel - sal\xe1rio exclusivamente vari\xe1vel.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2306remuneracao',
            name='vrsalfx',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2306supervisorestagio',
            name='cpfsupervisor',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='s2306supervisorestagio',
            name='nmsuperv',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
