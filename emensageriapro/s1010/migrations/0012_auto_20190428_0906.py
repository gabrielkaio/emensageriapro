# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1010', '0011_auto_20190427_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codinccp',
            field=models.CharField(choices=[(b'00', '00 - N\xe3o \xe9 base de c\xe1lculo'), (b'01', '01 - N\xe3o \xe9 base de c\xe1lculo em fun\xe7\xe3o de acordos internacionais de previd\xeancia social'), (b'11', '11 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Mensal'), (b'12', '12 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: 13o Sal\xe1rio'), (b'13', '13 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do Empregador - mensal'), (b'14', '14 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do Empregador - 13\xb0 sal\xe1rio'), (b'15', '15 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do segurado - mensal'), (b'16', '16 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do segurado - 13\xb0 sal\xe1rio'), (b'21', '21 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade mensal pago pelo Empregador'), (b'22', '22 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade - 13o Sal\xe1rio, pago pelo Empregador'), (b'23', '23 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Auxilio doen\xe7a mensal - Regime Pr\xf3prio de Previd\xeancia Social'), (b'24', '24 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Auxilio doen\xe7a 13o sal\xe1rio doen\xe7a - Regime pr\xf3prio de previd\xeancia social'), (b'25', '25 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade mensal pago pelo INSS'), (b'26', '26 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade - 13\xb0 sal\xe1rio, pago pelo INSS'), (b'31', '31 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: Mensal'), (b'32', '32 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: 13o Sal\xe1rio'), (b'34', '34 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: SEST'), (b'35', '35 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: SENAT'), (b'51', '51 - Outros: Sal\xe1rio-fam\xedlia'), (b'61', '61 - Outros: Complemento de sal\xe1rio-m\xednimo - Regime pr\xf3prio de previd\xeancia social'), (b'91', '91 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Mensal'), (b'92', '92 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: 13o Sal\xe1rio'), (b'93', '93 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Sal\xe1rio maternidade'), (b'94', '94 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Sal\xe1rio maternidade 13o sal\xe1rio'), (b'95', '95 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - mensal'), (b'96', '96 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - 13\xba sal\xe1rio'), (b'97', '97 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - Sal\xe1rio maternidade'), (b'98', '98 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - Sal\xe1rio maternidade 13\xba sal\xe1rio')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codincfgts',
            field=models.CharField(choices=[(b'00', '00 - N\xe3o \xe9 Base de C\xe1lculo do FGTS'), (b'11', '11 - Base de C\xe1lculo do FGTS'), (b'12', '12 - Base de C\xe1lculo do FGTS 13\xb0 sal\xe1rio'), (b'21', '21 - Base de C\xe1lculo do FGTS Rescis\xf3rio (aviso pr\xe9vio)'), (b'91', '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codincirrf',
            field=models.CharField(choices=[(b'00', '00 - Rendimento n\xe3o tribut\xe1vel'), (b'01', '01 - Rendimento n\xe3o tribut\xe1vel em fun\xe7\xe3o de acordos internacionais de bitributa\xe7\xe3o'), (b'09', '09 - Outras verbas n\xe3o consideradas como base de c\xe1lculo ou rendimento'), (b'11', '11 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: Remunera\xe7\xe3o mensal'), (b'12', '12 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: 13o Sal\xe1rio'), (b'13', '13 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: F\xe9rias'), (b'14', '14 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: PLR'), (b'15', '15 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: Rendimentos Recebidos Acumuladamente - RRA'), (b'31', '31 - Reten\xe7\xf5es do IRRF efetuadas sobre: Remunera\xe7\xe3o mensal'), (b'32', '32 - Reten\xe7\xf5es do IRRF efetuadas sobre: 13o Sal\xe1rio'), (b'33', '33 - Reten\xe7\xf5es do IRRF efetuadas sobre: F\xe9rias'), (b'34', '34 - Reten\xe7\xf5es do IRRF efetuadas sobre: PLR'), (b'35', '35 - Reten\xe7\xf5es do IRRF efetuadas sobre: RRA'), (b'41', '41 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Previd\xeancia Social Oficial - PSO - Remuner. mensal'), (b'42', '42 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: PSO - 13\xb0 sal\xe1rio'), (b'43', '43 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: PSO - F\xe9rias'), (b'44', '44 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: PSO - RRA'), (b'46', '46 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Previd\xeancia Privada - sal\xe1rio mensal'), (b'47', '47 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Previd\xeancia Privada - 13\xb0 sal\xe1rio'), (b'51', '51 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - Remunera\xe7\xe3o mensal'), (b'52', '52 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - 13\xb0 sal\xe1rio'), (b'53', '53 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - F\xe9rias'), (b'54', '54 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - PLR'), (b'55', '55 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - RRA'), (b'61', '61 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - Remunera\xe7\xe3o mensal'), (b'62', '62 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - 13\xb0 sal\xe1rio'), (b'63', '63 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - Remunera\xe7\xe3o mensal'), (b'64', '64 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - 13\xb0 sal\xe1rio'), (b'70', '70 - Isen\xe7\xf5es do IRRF: Parcela Isenta 65 anos - Remunera\xe7\xe3o mensal'), (b'71', '71 - Isen\xe7\xf5es do IRRF: Parcela Isenta 65 anos - 13\xb0 sal\xe1rio'), (b'72', '72 - Isen\xe7\xf5es do IRRF: Di\xe1rias'), (b'73', '73 - Isen\xe7\xf5es do IRRF: Ajuda de custo'), (b'74', '74 - Isen\xe7\xf5es do IRRF: Indeniza\xe7\xe3o e rescis\xe3o de contrato, inclusive a t\xedtulo de PDV e acidentes de trabalho'), (b'75', '75 - Isen\xe7\xf5es do IRRF: Abono pecuni\xe1rio'), (b'76', '76 - Isen\xe7\xf5es do IRRF: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - Remunera\xe7\xe3o Mensal'), (b'77', '77 - Isen\xe7\xf5es do IRRF: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - 13\xb0 sal\xe1rio'), (b'78', '78 - Isen\xe7\xf5es do IRRF: Valores pagos a titular ou s\xf3cio de microempresa ou empresa de pequeno porte, exceto pr\xf3-labore e alugueis'), (b'79', '79 - Isen\xe7\xf5es do IRRF: Outras isen\xe7\xf5es (o nome da rubrica deve ser claro para identifica\xe7\xe3o da natureza dos valores)'), (b'81', '81 - Demandas Judiciais: Dep\xf3sito judicial'), (b'82', '82 - Demandas Judiciais: Compensa\xe7\xe3o judicial do ano calend\xe1rio'), (b'83', '83 - Demandas Judiciais: Compensa\xe7\xe3o judicial de anos anteriores'), (b'91', '91 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: Remunera\xe7\xe3o mensal'), (b'92', '92 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: 13o Sal\xe1rio'), (b'93', '93 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: F\xe9rias'), (b'94', '94 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: PLR'), (b'95', '95 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: RRA')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codincsind',
            field=models.CharField(choices=[(b'00', '00 - N\xe3o \xe9 base de c\xe1lculo'), (b'11', '11 - Base de c\xe1lculo'), (b'31', '31 - Valor da contribui\xe7\xe3o sindical laboral descontada'), (b'91', '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='codrubr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='dscrubr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='idetabrubr',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='natrubr',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='s1010_evttabrubrica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracao_s1010_evttabrubrica', to='esocial.s1010evtTabRubrica'),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='tprubr',
            field=models.IntegerField(choices=[(1, '1 - Vencimento, provento ou pens\xe3o'), (2, '2 - Desconto'), (3, '3 - Informativa'), (4, '4 - Informativa dedutora')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='codsusp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='extdecisao',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico'), (1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico + Descontada dos Segurados'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal + Descontada dos Segurados'), (3, '3 - Contribui\xe7\xe3o Previdenci\xe1ria Descontada dos Segurados')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='s1010_alteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracaoideprocessocp_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocprp',
            name='extdecisao',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico'), (1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico + Descontada dos Segurados'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal + Descontada dos Segurados'), (3, '3 - Contribui\xe7\xe3o Previdenci\xe1ria Descontada dos Segurados')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocprp',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocprp',
            name='s1010_alteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracaoideprocessocprp_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocprp',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessofgts',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessofgts',
            name='s1010_alteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracaoideprocessofgts_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessoirrf',
            name='codsusp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessoirrf',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessoirrf',
            name='s1010_alteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracaoideprocessoirrf_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessosind',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessosind',
            name='s1010_alteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracaoideprocessosind_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
        migrations.AlterField(
            model_name='s1010alteracaonovavalidade',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1010alteracaonovavalidade',
            name='s1010_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1010alteracaonovavalidade_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
        migrations.AlterField(
            model_name='s1010exclusao',
            name='codrubr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1010exclusao',
            name='idetabrubr',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1010exclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1010exclusao',
            name='s1010_evttabrubrica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1010exclusao_s1010_evttabrubrica', to='esocial.s1010evtTabRubrica'),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codinccp',
            field=models.CharField(choices=[(b'00', '00 - N\xe3o \xe9 base de c\xe1lculo'), (b'01', '01 - N\xe3o \xe9 base de c\xe1lculo em fun\xe7\xe3o de acordos internacionais de previd\xeancia social'), (b'11', '11 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Mensal'), (b'12', '12 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: 13o Sal\xe1rio'), (b'13', '13 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do Empregador - mensal'), (b'14', '14 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do Empregador - 13\xb0 sal\xe1rio'), (b'15', '15 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do segurado - mensal'), (b'16', '16 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Exclusiva do segurado - 13\xb0 sal\xe1rio'), (b'21', '21 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade mensal pago pelo Empregador'), (b'22', '22 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade - 13o Sal\xe1rio, pago pelo Empregador'), (b'23', '23 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Auxilio doen\xe7a mensal - Regime Pr\xf3prio de Previd\xeancia Social'), (b'24', '24 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Auxilio doen\xe7a 13o sal\xe1rio doen\xe7a - Regime pr\xf3prio de previd\xeancia social'), (b'25', '25 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade mensal pago pelo INSS'), (b'26', '26 - Base de c\xe1lculo das contribui\xe7\xf5es sociais - Sal\xe1rio de Contribui\xe7\xe3o: Sal\xe1rio maternidade - 13\xb0 sal\xe1rio, pago pelo INSS'), (b'31', '31 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: Mensal'), (b'32', '32 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: 13o Sal\xe1rio'), (b'34', '34 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: SEST'), (b'35', '35 - Contribui\xe7\xe3o descontada do Segurado sobre sal\xe1rio de contribui\xe7\xe3o: SENAT'), (b'51', '51 - Outros: Sal\xe1rio-fam\xedlia'), (b'61', '61 - Outros: Complemento de sal\xe1rio-m\xednimo - Regime pr\xf3prio de previd\xeancia social'), (b'91', '91 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Mensal'), (b'92', '92 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: 13o Sal\xe1rio'), (b'93', '93 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Sal\xe1rio maternidade'), (b'94', '94 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Sal\xe1rio maternidade 13o sal\xe1rio'), (b'95', '95 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - mensal'), (b'96', '96 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - 13\xba sal\xe1rio'), (b'97', '97 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - Sal\xe1rio maternidade'), (b'98', '98 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Exclusiva do Empregador - Sal\xe1rio maternidade 13\xba sal\xe1rio')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codincfgts',
            field=models.CharField(choices=[(b'00', '00 - N\xe3o \xe9 Base de C\xe1lculo do FGTS'), (b'11', '11 - Base de C\xe1lculo do FGTS'), (b'12', '12 - Base de C\xe1lculo do FGTS 13\xb0 sal\xe1rio'), (b'21', '21 - Base de C\xe1lculo do FGTS Rescis\xf3rio (aviso pr\xe9vio)'), (b'91', '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codincirrf',
            field=models.CharField(choices=[(b'00', '00 - Rendimento n\xe3o tribut\xe1vel'), (b'01', '01 - Rendimento n\xe3o tribut\xe1vel em fun\xe7\xe3o de acordos internacionais de bitributa\xe7\xe3o'), (b'09', '09 - Outras verbas n\xe3o consideradas como base de c\xe1lculo ou rendimento'), (b'11', '11 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: Remunera\xe7\xe3o mensal'), (b'12', '12 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: 13o Sal\xe1rio'), (b'13', '13 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: F\xe9rias'), (b'14', '14 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: PLR'), (b'15', '15 - Rendimentos tribut\xe1veis - base de c\xe1lculo do IRRF: Rendimentos Recebidos Acumuladamente - RRA'), (b'31', '31 - Reten\xe7\xf5es do IRRF efetuadas sobre: Remunera\xe7\xe3o mensal'), (b'32', '32 - Reten\xe7\xf5es do IRRF efetuadas sobre: 13o Sal\xe1rio'), (b'33', '33 - Reten\xe7\xf5es do IRRF efetuadas sobre: F\xe9rias'), (b'34', '34 - Reten\xe7\xf5es do IRRF efetuadas sobre: PLR'), (b'35', '35 - Reten\xe7\xf5es do IRRF efetuadas sobre: RRA'), (b'41', '41 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Previd\xeancia Social Oficial - PSO - Remuner. mensal'), (b'42', '42 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: PSO - 13\xb0 sal\xe1rio'), (b'43', '43 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: PSO - F\xe9rias'), (b'44', '44 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: PSO - RRA'), (b'46', '46 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Previd\xeancia Privada - sal\xe1rio mensal'), (b'47', '47 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Previd\xeancia Privada - 13\xb0 sal\xe1rio'), (b'51', '51 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - Remunera\xe7\xe3o mensal'), (b'52', '52 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - 13\xb0 sal\xe1rio'), (b'53', '53 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - F\xe9rias'), (b'54', '54 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - PLR'), (b'55', '55 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Pens\xe3o Aliment\xedcia - RRA'), (b'61', '61 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - Remunera\xe7\xe3o mensal'), (b'62', '62 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - 13\xb0 sal\xe1rio'), (b'63', '63 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - Remunera\xe7\xe3o mensal'), (b'64', '64 - Dedu\xe7\xf5es da base de c\xe1lculo do IRRF: Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - 13\xb0 sal\xe1rio'), (b'70', '70 - Isen\xe7\xf5es do IRRF: Parcela Isenta 65 anos - Remunera\xe7\xe3o mensal'), (b'71', '71 - Isen\xe7\xf5es do IRRF: Parcela Isenta 65 anos - 13\xb0 sal\xe1rio'), (b'72', '72 - Isen\xe7\xf5es do IRRF: Di\xe1rias'), (b'73', '73 - Isen\xe7\xf5es do IRRF: Ajuda de custo'), (b'74', '74 - Isen\xe7\xf5es do IRRF: Indeniza\xe7\xe3o e rescis\xe3o de contrato, inclusive a t\xedtulo de PDV e acidentes de trabalho'), (b'75', '75 - Isen\xe7\xf5es do IRRF: Abono pecuni\xe1rio'), (b'76', '76 - Isen\xe7\xf5es do IRRF: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - Remunera\xe7\xe3o Mensal'), (b'77', '77 - Isen\xe7\xf5es do IRRF: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - 13\xb0 sal\xe1rio'), (b'78', '78 - Isen\xe7\xf5es do IRRF: Valores pagos a titular ou s\xf3cio de microempresa ou empresa de pequeno porte, exceto pr\xf3-labore e alugueis'), (b'79', '79 - Isen\xe7\xf5es do IRRF: Outras isen\xe7\xf5es (o nome da rubrica deve ser claro para identifica\xe7\xe3o da natureza dos valores)'), (b'81', '81 - Demandas Judiciais: Dep\xf3sito judicial'), (b'82', '82 - Demandas Judiciais: Compensa\xe7\xe3o judicial do ano calend\xe1rio'), (b'83', '83 - Demandas Judiciais: Compensa\xe7\xe3o judicial de anos anteriores'), (b'91', '91 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: Remunera\xe7\xe3o mensal'), (b'92', '92 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: 13o Sal\xe1rio'), (b'93', '93 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: F\xe9rias'), (b'94', '94 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: PLR'), (b'95', '95 - Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre: RRA')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codincsind',
            field=models.CharField(choices=[(b'00', '00 - N\xe3o \xe9 base de c\xe1lculo'), (b'11', '11 - Base de c\xe1lculo'), (b'31', '31 - Valor da contribui\xe7\xe3o sindical laboral descontada'), (b'91', '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='codrubr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='dscrubr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='idetabrubr',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='natrubr',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='s1010_evttabrubrica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1010inclusao_s1010_evttabrubrica', to='esocial.s1010evtTabRubrica'),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='tprubr',
            field=models.IntegerField(choices=[(1, '1 - Vencimento, provento ou pens\xe3o'), (2, '2 - Desconto'), (3, '3 - Informativa'), (4, '4 - Informativa dedutora')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='codsusp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='extdecisao',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico'), (1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico + Descontada dos Segurados'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal + Descontada dos Segurados'), (3, '3 - Contribui\xe7\xe3o Previdenci\xe1ria Descontada dos Segurados')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='s1010_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010inclusaoideprocessocp_s1010_inclusao', to='s1010.s1010inclusao'),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocprp',
            name='extdecisao',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico'), (1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico + Descontada dos Segurados'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal + Descontada dos Segurados'), (3, '3 - Contribui\xe7\xe3o Previdenci\xe1ria Descontada dos Segurados')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocprp',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocprp',
            name='s1010_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010inclusaoideprocessocprp_s1010_inclusao', to='s1010.s1010inclusao'),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocprp',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessofgts',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessofgts',
            name='s1010_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010inclusaoideprocessofgts_s1010_inclusao', to='s1010.s1010inclusao'),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessoirrf',
            name='codsusp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessoirrf',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessoirrf',
            name='s1010_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010inclusaoideprocessoirrf_s1010_inclusao', to='s1010.s1010inclusao'),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessosind',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessosind',
            name='s1010_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1010inclusaoideprocessosind_s1010_inclusao', to='s1010.s1010inclusao'),
        ),
    ]
