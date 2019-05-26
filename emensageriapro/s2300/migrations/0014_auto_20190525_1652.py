# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2300', '0013_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2300afastamento',
            name='codmotafast',
            field=models.CharField(choices=[(b'01', '01 - Acidente/Doen\xe7a do trabalho'), (b'03', '03 - Acidente/Doen\xe7a n\xe3o relacionada ao trabalho'), (b'05', '05 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), sem remunera\xe7\xe3o'), (b'06', '06 - Aposentadoria por invalidez'), (b'07', '07 - Acompanhamento - Licen\xe7a para acompanhamento de membro da fam\xedlia enfermo'), (b'08', '08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, \xa76\xba, Dec. 99.684/90 (Regulamento do FGTS)'), (b'10', '10 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), com remunera\xe7\xe3o'), (b'11', '11 - C\xe1rcere'), (b'12', '12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25\xb0, par\xe1grafo \xfanico - Celetistas em geral'), (b'13', '13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1\xb0, inciso II, al\xednea \u201cl\u201d - Servidor p\xfablico, estatut\xe1rio ou n\xe3o, dos \xf3rg\xe3os ou entidades da Administra\xe7\xe3o Direta ou Indireta da Uni\xe3o, dos Estados, do Distrito Federal, dos Munic\xedpios e dos Territ\xf3rios, inclusive das funda\xe7\xf5es mantidas pelo Poder P\xfablico'), (b'14', '14 - Cess\xe3o / Requisi\xe7\xe3o'), (b'15', '15 - Gozo de f\xe9rias ou recesso - Afastamento tempor\xe1rio para o gozo de f\xe9rias ou recesso'), (b'16', '16 - Licen\xe7a remunerada - Lei, liberalidade da empresa ou Acordo/Conven\xe7\xe3o Coletiva de Trabalho'), (b'17', '17 - Licen\xe7a Maternidade - 120 dias e suas prorroga\xe7\xf5es/antecipa\xe7\xf5es, inclusive para o c\xf4njuge sobrevivente'), (b'17', '17 - Licen\xe7a Maternidade - 120 dias, inclusive para o c\xf4njuge sobrevivente'), (b'18', '18 - Licen\xe7a Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidad\xe3), inclusive para o c\xf4njuge sobrevivente'), (b'19', '19 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de aborto n\xe3o criminoso'), (b'20', '20 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de licen\xe7a- maternidade decorrente de ado\xe7\xe3o ou guarda judicial de crian\xe7a, inclusive para o c\xf4njuge sobrevivente'), (b'21', '21 - Licen\xe7a n\xe3o remunerada ou Sem Vencimento'), (b'22', '22 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, sem remunera\xe7\xe3o'), (b'23', '23 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, com remunera\xe7\xe3o'), (b'24', '24 - Mandato Sindical - Afastamento tempor\xe1rio para exerc\xedcio de mandato sindical'), (b'25', '25 - Mulher v\xedtima de viol\xeancia - Lei 11.340/2006 - art. 9\xba \xa72o, II - Lei Maria da Penha'), (b'26', '26 - Participa\xe7\xe3o de empregado no Conselho Nacional de Previd\xeancia Social-CNPS (art. 3\xba, Lei 8.213/1991)'), (b'27', '27 - Qualifica\xe7\xe3o - Afastamento por suspens\xe3o do contrato de acordo com o art 476-A da CLT'), (b'28', '28 - Representante Sindical - Afastamento pelo tempo que se fizer necess\xe1rio, quando, na qualidade de representante de entidade sindical, estiver participando de reuni\xe3o oficial de organismo internacional do qual o Brasil seja membro'), (b'29', '29 - Servi\xe7o Militar - Afastamento tempor\xe1rio para prestar servi\xe7o militar obrigat\xf3rio'), (b'30', '30 - Suspens\xe3o disciplinar - CLT, art. 474'), (b'31', '31 - Servidor P\xfablico em Disponibilidade'), (b'33', '33 - Licen\xe7a Maternidade - de 180 dias, Lei 13.301/2016'), (b'34', '34 - Inatividade do trabalhador avulso (portu\xe1rio ou n\xe3o portu\xe1rio) por per\xedodo superior a 90 dias'), (b'35', '35 - Licen\xe7a Maternidade - Antecipa\xe7\xe3o e/ou prorroga\xe7\xe3o mediante atestado m\xe9dico')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300afastamento',
            name='dtiniafast',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='cep',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='cnpjagntinteg',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='dsclograd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='nmrazao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='nrlograd',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ageintegracao',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='cep',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='codmunic',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='dsclograd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='nrlograd',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='tplograd',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300brasil',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300cargofuncao',
            name='codcargo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='categoriacnh',
            field=models.CharField(choices=[(b'A', 'A'), (b'AB', 'AB'), (b'AC', 'AC'), (b'AD', 'AD'), (b'AE', 'AE'), (b'B', 'B'), (b'C', 'C'), (b'D', 'D'), (b'E', 'E')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='dtvalid',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='nrregcnh',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='s2300cnh',
            name='ufcnh',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='nrctps',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='seriectps',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ctps',
            name='ufctps',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='depirrf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='depsf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='dtnascto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='inctrab',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='nmdep',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='s2300dependente',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='dsclograd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='nmcid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='nrlograd',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='s2300exterior',
            name='paisresid',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300fgts',
            name='opcfgts',
            field=models.IntegerField(choices=[(1, '1 - Optante'), (2, '2 - N\xe3o Optante.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defauditiva',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='deffisica',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defintelectual',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defmental',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='defvisual',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodeficiencia',
            name='reabreadap',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infodirigentesindical',
            name='categorig',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='dtprevterm',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='natestagio',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o Obrigat\xf3rio.'), (b'O', 'O - Obrigat\xf3rio')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='nivestagio',
            field=models.IntegerField(choices=[(1, '1 - Fundamental'), (2, '2 - M\xe9dio'), (3, '3 - Forma\xe7\xe3o Profissional'), (4, '4 - Superior'), (8, '8 - Especial'), (9, '9 - M\xe3e social. (Lei 7644, de 1987).')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300infoestagiario',
            name='nmrazao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='categorig',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='cnpjcednt',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='dtadmced',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='infonus',
            field=models.IntegerField(choices=[(1, '1 - \xd4nus do Cedente'), (2, '2 - \xd4nus do Cession\xe1rio'), (3, '3 - \xd4nus do Cedente e Cession\xe1rio.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='matricced',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='tpregprev',
            field=models.IntegerField(choices=[(1, '1 - Regime Geral da Previd\xeancia Social - RGPS'), (2, '2 - Regime Pr\xf3prio de Previd\xeancia Social - RPPS'), (3, '3 - Regime de Previd\xeancia Social no Exterior.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300infotrabcedido',
            name='tpregtrab',
            field=models.IntegerField(choices=[(1, '1 - CLT - Consolida\xe7\xe3o das Leis de Trabalho e legisla\xe7\xf5es trabalhistas espec\xedficas'), (2, '2 - Estatut\xe1rio.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300mudancacpf',
            name='cpfant',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='s2300mudancacpf',
            name='dtaltcpf',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300oc',
            name='nroc',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2300oc',
            name='orgaoemissor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2300remuneracao',
            name='undsalfixo',
            field=models.IntegerField(choices=[(1, '1 - Por Hora'), (2, '2 - Por Dia'), (3, '3 - Por Semana'), (4, '4 - Por Quinzena'), (5, '5 - Por M\xeas'), (6, '6 - Por Tarefa'), (7, '7 - N\xe3o aplic\xe1vel - sal\xe1rio exclusivamente vari\xe1vel.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300remuneracao',
            name='vrsalfx',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s2300rg',
            name='nrrg',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2300rg',
            name='orgaoemissor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ric',
            name='nrric',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2300ric',
            name='orgaoemissor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2300rne',
            name='nrrne',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='s2300rne',
            name='orgaoemissor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2300supervisorestagio',
            name='cpfsupervisor',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='s2300supervisorestagio',
            name='nmsuperv',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='s2300termino',
            name='dtterm',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='casadobr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='classtrabestrang',
            field=models.IntegerField(choices=[(1, '1 - Visto permanente'), (10, '10 - Beneficiado pelo acordo entre pa\xedses do Mercosul'), (11, '11 - Dependente de agente diplom\xe1tico e/ou consular de pa\xedses que mant\xe9m conv\xeanio de reciprocidade para o exerc\xedcio de atividade remunerada no Brasil'), (12, '12 - Beneficiado pelo Tratado de Amizade, Coopera\xe7\xe3o e Consulta entre a Rep\xfablica Federativa do Brasil e a Rep\xfablica Portuguesa.'), (2, '2 - Visto tempor\xe1rio'), (3, '3 - Asilado'), (4, '4 - Refugiado'), (5, '5 - Solicitante de Ref\xfagio'), (6, '6 - Residente fora do Brasil'), (7, '7 - Deficiente f\xedsico e com mais de 51 anos'), (8, '8 - Com resid\xeancia provis\xf3ria e anistiado, em situa\xe7\xe3o irregular'), (9, '9 - Perman\xeancia no Brasil em raz\xe3o de filhos ou c\xf4njuge brasileiros')], null=True),
        ),
        migrations.AlterField(
            model_name='s2300trabestrangeiro',
            name='filhosbr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
    ]
