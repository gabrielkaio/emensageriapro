# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1000', '0004_auto_20181118_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1000alteracao',
            name='classtrib',
            field=models.CharField(choices=[(b'01', '01 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda'), (b'02', '02 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria n\xe3o substitu\xedda'), (b'03', '03 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda e n\xe3o substitu\xedda'), (b'04', '04 - MEI - Micro Empreendedor Individual'), (b'06', '06 - Agroind\xfastria'), (b'07', '07 - Produtor Rural Pessoa Jur\xeddica'), (b'08', '08 - Cons\xf3rcio Simplificado de Produtores Rurais'), (b'09', '09 - \xd3rg\xe3o Gestor de M\xe3o de Obra'), (b'10', '10 - Entidade Sindical a que se refere a Lei 12.023/2009'), (b'11', '11 - Associa\xe7\xe3o Desportiva que mant\xe9m Clube de Futebol Profissional'), (b'13', '13 - Banco, caixa econ\xf4mica, sociedade de cr\xe9dito, financiamento e investimento e demais empresas relacionadas no par\xe1grafo 1\xba do art. 22 da Lei 8.212./91'), (b'14', '14 - Sindicatos em geral, exceto aquele classificado no c\xf3digo [10]'), (b'21', '21 - Pessoa F\xedsica, exceto Segurado Especial'), (b'22', '22 - Segurado Especial'), (b'60', '60 - Miss\xe3o Diplom\xe1tica ou Reparti\xe7\xe3o Consular de carreira estrangeira'), (b'70', '70 - Empresa de que trata o Decreto 5.436/2005'), (b'80', '80 - Entidade Beneficente de Assist\xeancia Social isenta de contribui\xe7\xf5es sociais'), (b'85', '85 - Ente Federativo, \xd3rg\xe3os da Uni\xe3o, Autarquias e Funda\xe7\xf5es P\xfablicas'), (b'99', '99 - Pessoas Jur\xeddicas em Geral')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='cpfctt',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='inddesfolha',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o Aplic\xe1vel'), (1, '1 - Empresa enquadrada nos art. 7\xba a 9\xba da Lei 12.546/2011')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='indett',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 Empresa de Trabalho Tempor\xe1rio'), (b'S', 'S - Empresa de Trabalho Tempor\xe1rio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='indoptregeletron',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o optou pelo registro eletr\xf4nico de empregados'), (1, '1 - Optou pelo registro eletr\xf4nico de empregados')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='nmctt',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='nmrazao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='s1000_evtinfoempregador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracao_s1000_evtinfoempregador', to='esocial.s1000evtInfoEmpregador'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='dtemiscertif',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='dtvenccertif',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='ideminlei',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='nrcertif',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='s1000_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaodadosisencao_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='ideefr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='indrpps',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='prevcomp',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='s1000_alteracao_infoop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaoinfoefr_s1000_alteracao_infoop', to='s1000.s1000alteracaoinfoOP'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='indrpps',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='nmente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='s1000_alteracao_infoop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaoinfoente_s1000_alteracao_infoop', to='s1000.s1000alteracaoinfoOP'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='subteto',
            field=models.IntegerField(choices=[(1, '1 - Executivo'), (2, '2 - Judici\xe1rio'), (3, '3 - Legislativo'), (9, '9 - Todos os poderes')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='vrsubteto',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='ideefr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='indugrpps',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='nrsiafi',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='poderop',
            field=models.IntegerField(choices=[(1, '1 - Executivo'), (2, '2 - Judici\xe1rio'), (3, '3 - Legislativo'), (4, '4 - Minist\xe9rio P\xfablico'), (5, '5 - Tribunal de Contas'), (6, '6 - Defensoria P\xfablica')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='s1000_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaoinfoop_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='vrtetorem',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoorginternacional',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoorginternacional',
            name='indacordoisenmulta',
            field=models.IntegerField(choices=[(0, '0 - Sem acordo'), (1, '1 - Com acordo')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoorginternacional',
            name='s1000_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaoinfoorginternacional_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaonovavalidade',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaonovavalidade',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1000alteracaonovavalidade',
            name='s1000_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaonovavalidade_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopf',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopf',
            name='indsitpf',
            field=models.IntegerField(choices=[(0, '0 - Situa\xe7\xe3o Normal'), (1, '1 - Encerramento de esp\xf3lio'), (2, '2 - Sa\xedda do pa\xeds em car\xe1ter permanente')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopf',
            name='s1000_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaosituacaopf_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopj',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopj',
            name='indsitpj',
            field=models.IntegerField(choices=[(0, '0 - Situa\xe7\xe3o Normal'), (1, '1 - Extin\xe7\xe3o'), (2, '2 - Fus\xe3o'), (3, '3 - Cis\xe3o'), (4, '4 - Incorpora\xe7\xe3o')]),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopj',
            name='s1000_alteracao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaosituacaopj_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='cnpjsofthouse',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='nmcont',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='nmrazao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='s1000_alteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1000alteracaosoftwarehouse_s1000_alteracao', to='s1000.s1000alteracao'),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='telefone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='s1000exclusao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000exclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1000exclusao',
            name='s1000_evtinfoempregador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000exclusao_s1000_evtinfoempregador', to='esocial.s1000evtInfoEmpregador'),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='classtrib',
            field=models.CharField(choices=[(b'01', '01 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda'), (b'02', '02 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria n\xe3o substitu\xedda'), (b'03', '03 - Empresa enquadrada no regime de tributa\xe7\xe3o Simples Nacional com tributa\xe7\xe3o previdenci\xe1ria substitu\xedda e n\xe3o substitu\xedda'), (b'04', '04 - MEI - Micro Empreendedor Individual'), (b'06', '06 - Agroind\xfastria'), (b'07', '07 - Produtor Rural Pessoa Jur\xeddica'), (b'08', '08 - Cons\xf3rcio Simplificado de Produtores Rurais'), (b'09', '09 - \xd3rg\xe3o Gestor de M\xe3o de Obra'), (b'10', '10 - Entidade Sindical a que se refere a Lei 12.023/2009'), (b'11', '11 - Associa\xe7\xe3o Desportiva que mant\xe9m Clube de Futebol Profissional'), (b'13', '13 - Banco, caixa econ\xf4mica, sociedade de cr\xe9dito, financiamento e investimento e demais empresas relacionadas no par\xe1grafo 1\xba do art. 22 da Lei 8.212./91'), (b'14', '14 - Sindicatos em geral, exceto aquele classificado no c\xf3digo [10]'), (b'21', '21 - Pessoa F\xedsica, exceto Segurado Especial'), (b'22', '22 - Segurado Especial'), (b'60', '60 - Miss\xe3o Diplom\xe1tica ou Reparti\xe7\xe3o Consular de carreira estrangeira'), (b'70', '70 - Empresa de que trata o Decreto 5.436/2005'), (b'80', '80 - Entidade Beneficente de Assist\xeancia Social isenta de contribui\xe7\xf5es sociais'), (b'85', '85 - Ente Federativo, \xd3rg\xe3os da Uni\xe3o, Autarquias e Funda\xe7\xf5es P\xfablicas'), (b'99', '99 - Pessoas Jur\xeddicas em Geral')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='cpfctt',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='inddesfolha',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o Aplic\xe1vel'), (1, '1 - Empresa enquadrada nos art. 7\xba a 9\xba da Lei 12.546/2011')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='indett',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 Empresa de Trabalho Tempor\xe1rio'), (b'S', 'S - Empresa de Trabalho Tempor\xe1rio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='indoptregeletron',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o optou pelo registro eletr\xf4nico de empregados'), (1, '1 - Optou pelo registro eletr\xf4nico de empregados')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], max_length=7),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='nmctt',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='nmrazao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='s1000_evtinfoempregador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusao_s1000_evtinfoempregador', to='esocial.s1000evtInfoEmpregador'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='dtemiscertif',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='dtvenccertif',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='ideminlei',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='nrcertif',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='s1000_inclusao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaodadosisencao_s1000_inclusao', to='s1000.s1000inclusao'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='ideefr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='indrpps',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='prevcomp',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='s1000_inclusao_infoop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaoinfoefr_s1000_inclusao_infoop', to='s1000.s1000inclusaoinfoOP'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='indrpps',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='nmente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='s1000_inclusao_infoop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaoinfoente_s1000_inclusao_infoop', to='s1000.s1000inclusaoinfoOP'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='subteto',
            field=models.IntegerField(choices=[(1, '1 - Executivo'), (2, '2 - Judici\xe1rio'), (3, '3 - Legislativo'), (9, '9 - Todos os poderes')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='vrsubteto',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='ideefr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='indugrpps',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='nrsiafi',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='poderop',
            field=models.IntegerField(choices=[(1, '1 - Executivo'), (2, '2 - Judici\xe1rio'), (3, '3 - Legislativo'), (4, '4 - Minist\xe9rio P\xfablico'), (5, '5 - Tribunal de Contas'), (6, '6 - Defensoria P\xfablica')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='s1000_inclusao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaoinfoop_s1000_inclusao', to='s1000.s1000inclusao'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='vrtetorem',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoorginternacional',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoorginternacional',
            name='indacordoisenmulta',
            field=models.IntegerField(choices=[(0, '0 - Sem acordo'), (1, '1 - Com acordo')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoorginternacional',
            name='s1000_inclusao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaoinfoorginternacional_s1000_inclusao', to='s1000.s1000inclusao'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopf',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopf',
            name='indsitpf',
            field=models.IntegerField(choices=[(0, '0 - Situa\xe7\xe3o Normal'), (1, '1 - Encerramento de esp\xf3lio'), (2, '2 - Sa\xedda do pa\xeds em car\xe1ter permanente')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopf',
            name='s1000_inclusao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaosituacaopf_s1000_inclusao', to='s1000.s1000inclusao'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopj',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopj',
            name='indsitpj',
            field=models.IntegerField(choices=[(0, '0 - Situa\xe7\xe3o Normal'), (1, '1 - Extin\xe7\xe3o'), (2, '2 - Fus\xe3o'), (3, '3 - Cis\xe3o'), (4, '4 - Incorpora\xe7\xe3o')]),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopj',
            name='s1000_inclusao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaosituacaopj_s1000_inclusao', to='s1000.s1000inclusao'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='cnpjsofthouse',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='nmcont',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='nmrazao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='s1000_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1000inclusaosoftwarehouse_s1000_inclusao', to='s1000.s1000inclusao'),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='telefone',
            field=models.CharField(max_length=13),
        ),
    ]
