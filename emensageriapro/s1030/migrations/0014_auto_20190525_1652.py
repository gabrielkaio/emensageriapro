# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1030', '0013_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1030alteracao',
            name='codcargo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracao',
            name='codcbo',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracao',
            name='nmcargo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='acumcargo',
            field=models.IntegerField(choices=[(1, '1 - N\xe3o acumul\xe1vel'), (2, '2 - Profissional de Sa\xfade'), (3, '3 - Professor'), (4, '4 - T\xe9cnico/Cient\xedfico.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='contagemesp',
            field=models.IntegerField(choices=[(1, '1 - N\xe3o'), (2, '2 - Professor (Infantil, Fundamental e M\xe9dio)'), (3, '3 - Professor de Ensino Superior, Magistrado, Membro de Minist\xe9rio P\xfablico, Membro do Tribunal de Contas (com ingresso anterior a 16/12/1998 EC nr. 20/98)'), (4, '4 - Atividade de risco.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='dedicexcl',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='dtlei',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='nrlei',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='sitcargo',
            field=models.IntegerField(choices=[(1, '1 - Cria\xe7\xe3o'), (2, '2 - Extin\xe7\xe3o'), (3, '3 - Reestrutura\xe7\xe3o.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaonovavalidade',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1030exclusao',
            name='codcargo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1030exclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusao',
            name='codcargo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusao',
            name='codcbo',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusao',
            name='nmcargo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='acumcargo',
            field=models.IntegerField(choices=[(1, '1 - N\xe3o acumul\xe1vel'), (2, '2 - Profissional de Sa\xfade'), (3, '3 - Professor'), (4, '4 - T\xe9cnico/Cient\xedfico.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='contagemesp',
            field=models.IntegerField(choices=[(1, '1 - N\xe3o'), (2, '2 - Professor (Infantil, Fundamental e M\xe9dio)'), (3, '3 - Professor de Ensino Superior, Magistrado, Membro de Minist\xe9rio P\xfablico, Membro do Tribunal de Contas (com ingresso anterior a 16/12/1998 EC nr. 20/98)'), (4, '4 - Atividade de risco.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='dedicexcl',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='dtlei',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='nrlei',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='sitcargo',
            field=models.IntegerField(choices=[(1, '1 - Cria\xe7\xe3o'), (2, '2 - Extin\xe7\xe3o'), (3, '3 - Reestrutura\xe7\xe3o.')], null=True),
        ),
    ]
