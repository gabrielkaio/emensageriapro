# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r1070', '0011_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1070alteracao',
            name='indautoria',
            field=models.IntegerField(choices=[(1, '1 - Pr\xf3prio contribuinte'), (2, '2 - Outra entidade ou empresa.')], default=0),
        ),
        migrations.AlterField(
            model_name='r1070alteracao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1070alteracao',
            name='nrproc',
            field=models.CharField(default=b'A', max_length=21),
        ),
        migrations.AlterField(
            model_name='r1070alteracao',
            name='r1070_evttabprocesso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracao_r1070_evttabprocesso', to='efdreinf.r1070evtTabProcesso'),
        ),
        migrations.AlterField(
            model_name='r1070alteracao',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial.')], default=0),
        ),
        migrations.AlterField(
            model_name='r1070alteracaodadosprocjud',
            name='codmunic',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='r1070alteracaodadosprocjud',
            name='idvara',
            field=models.CharField(default=b'A', max_length=4),
        ),
        migrations.AlterField(
            model_name='r1070alteracaodadosprocjud',
            name='r1070_alteracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaodadosprocjud_r1070_alteracao', to='r1070.r1070alteracao'),
        ),
        migrations.AlterField(
            model_name='r1070alteracaodadosprocjud',
            name='ufvara',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='r1070alteracaoinfosusp',
            name='dtdecisao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='r1070alteracaoinfosusp',
            name='inddeposito',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='r1070alteracaoinfosusp',
            name='indsusp',
            field=models.CharField(choices=[(b'01', '01 - Liminar em Mandado de Seguran\xe7a'), (b'02', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'03', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'04', '04 - Antecipa\xe7\xe3o de Tutela'), (b'05', '05 - Liminar em Medida Cautelar'), (b'08', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'09', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade.')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='r1070alteracaoinfosusp',
            name='r1070_alteracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaoinfosusp_r1070_alteracao', to='r1070.r1070alteracao'),
        ),
        migrations.AlterField(
            model_name='r1070alteracaonovavalidade',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1070alteracaonovavalidade',
            name='r1070_alteracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070alteracaonovavalidade_r1070_alteracao', to='r1070.r1070alteracao'),
        ),
        migrations.AlterField(
            model_name='r1070exclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1070exclusao',
            name='nrproc',
            field=models.CharField(default=b'A', max_length=21),
        ),
        migrations.AlterField(
            model_name='r1070exclusao',
            name='r1070_evttabprocesso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070exclusao_r1070_evttabprocesso', to='efdreinf.r1070evtTabProcesso'),
        ),
        migrations.AlterField(
            model_name='r1070exclusao',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial.')], default=0),
        ),
        migrations.AlterField(
            model_name='r1070inclusao',
            name='indautoria',
            field=models.IntegerField(choices=[(1, '1 - Pr\xf3prio contribuinte'), (2, '2 - Outra entidade ou empresa.')], default=0),
        ),
        migrations.AlterField(
            model_name='r1070inclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1070inclusao',
            name='nrproc',
            field=models.CharField(default=b'A', max_length=21),
        ),
        migrations.AlterField(
            model_name='r1070inclusao',
            name='r1070_evttabprocesso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusao_r1070_evttabprocesso', to='efdreinf.r1070evtTabProcesso'),
        ),
        migrations.AlterField(
            model_name='r1070inclusao',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial.')], default=0),
        ),
        migrations.AlterField(
            model_name='r1070inclusaodadosprocjud',
            name='codmunic',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='r1070inclusaodadosprocjud',
            name='idvara',
            field=models.CharField(default=b'A', max_length=4),
        ),
        migrations.AlterField(
            model_name='r1070inclusaodadosprocjud',
            name='r1070_inclusao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusaodadosprocjud_r1070_inclusao', to='r1070.r1070inclusao'),
        ),
        migrations.AlterField(
            model_name='r1070inclusaodadosprocjud',
            name='ufvara',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='r1070inclusaoinfosusp',
            name='dtdecisao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='r1070inclusaoinfosusp',
            name='inddeposito',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='r1070inclusaoinfosusp',
            name='indsusp',
            field=models.CharField(choices=[(b'01', '01 - Liminar em Mandado de Seguran\xe7a'), (b'02', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'03', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'04', '04 - Antecipa\xe7\xe3o de Tutela'), (b'05', '05 - Liminar em Medida Cautelar'), (b'08', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'09', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade.')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='r1070inclusaoinfosusp',
            name='r1070_inclusao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1070inclusaoinfosusp_r1070_inclusao', to='r1070.r1070inclusao'),
        ),
    ]
