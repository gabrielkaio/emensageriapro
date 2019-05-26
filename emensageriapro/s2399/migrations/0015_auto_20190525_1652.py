# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2399', '0014_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2399detoper',
            name='cnpjoper',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detoper',
            name='regans',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detoper',
            name='vrpgtit',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detplano',
            name='dtnascto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2399detplano',
            name='nmdep',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detplano',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detplano',
            name='vlrpgdep',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detverbas',
            name='codrubr',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detverbas',
            name='idetabrubr',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='s2399detverbas',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2399dmdev',
            name='idedmdev',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s2399ideestablot',
            name='codlotacao',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s2399ideestablot',
            name='nrinsc',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2399ideestablot',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], null=True),
        ),
        migrations.AlterField(
            model_name='s2399infoagnocivo',
            name='grauexp',
            field=models.IntegerField(choices=[(1, '1 - Na\u0303o ensejador de aposentadoria especial'), (2, '2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuic\u0327a\u0303o e ali\u0301quota de 12%)'), (3, '3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuic\u0327a\u0303o e ali\u0301quota de 9%)'), (4, '4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuic\u0327a\u0303o e ali\u0301quota de 6%).')], null=True),
        ),
        migrations.AlterField(
            model_name='s2399infomv',
            name='indmv',
            field=models.IntegerField(choices=[(1, '1 - O declarante aplica a al\xedquota de desconto do segurado sobre a remunera\xe7\xe3o por ele informada (o percentual da al\xedquota ser\xe1 obtido considerando a remunera\xe7\xe3o total do trabalhador)'), (2, '2 - O declarante aplica a al\xedquota de desconto do segurado sobre a diferen\xe7a entre o limite m\xe1ximo do sal\xe1rio de contribui\xe7\xe3o e a remunera\xe7\xe3o de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'), (3, '3 - O declarante n\xe3o realiza desconto do segurado, uma vez que houve desconto sobre o limite m\xe1ximo de sal\xe1rio de contribui\xe7\xe3o em outra(s) empresa(s).')], null=True),
        ),
        migrations.AlterField(
            model_name='s2399infosimples',
            name='indsimples',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Substitu\xedda Integralmente'), (2, '2 - Contribui\xe7\xe3o n\xe3o substitu\xedda'), (3, '3 - Contribui\xe7\xe3o n\xe3o substitu\xedda concomitante com contribui\xe7\xe3o substitu\xedda.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2399mudancacpf',
            name='novocpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='s2399procjudtrab',
            name='nrprocjud',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2399procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(1, '1 - IRRF'), (2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2399quarentena',
            name='dtfimquar',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2399remunoutrempr',
            name='codcateg',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s2399remunoutrempr',
            name='nrinsc',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2399remunoutrempr',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], null=True),
        ),
        migrations.AlterField(
            model_name='s2399remunoutrempr',
            name='vlrremunoe',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]