# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2230', '0008_auto_20190204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2230emitente',
            name='ideoc',
            field=models.IntegerField(choices=[(1, '1 - Conselho Regional de Medicina (CRM)'), (2, '2 - Conselho Regional de Odontologia (CRO)'), (3, '3 - Registro do Minist\xe9rio da Sa\xfade (RMS)')], default=0),
        ),
        migrations.AlterField(
            model_name='s2230emitente',
            name='nmemit',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s2230emitente',
            name='nroc',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2230emitente',
            name='s2230_infoatestado',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230emitente_s2230_infoatestado', to='s2230.s2230infoAtestado'),
        ),
        migrations.AlterField(
            model_name='s2230fimafastamento',
            name='dttermafast',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2230fimafastamento',
            name='s2230_evtafasttemp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230fimafastamento_s2230_evtafasttemp', to='esocial.s2230evtAfastTemp'),
        ),
        migrations.AlterField(
            model_name='s2230infoatestado',
            name='qtddiasafast',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s2230infoatestado',
            name='s2230_iniafastamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230infoatestado_s2230_iniafastamento', to='s2230.s2230iniAfastamento'),
        ),
        migrations.AlterField(
            model_name='s2230infocessao',
            name='cnpjcess',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2230infocessao',
            name='infonus',
            field=models.IntegerField(choices=[(1, '1 - \xd4nus do Cedente'), (2, '2 - \xd4nus do Cession\xe1rio'), (3, '3 - \xd4nus do Cedente e Cession\xe1rio')], default=0),
        ),
        migrations.AlterField(
            model_name='s2230infocessao',
            name='s2230_iniafastamento',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230infocessao_s2230_iniafastamento', to='s2230.s2230iniAfastamento'),
        ),
        migrations.AlterField(
            model_name='s2230infomandsind',
            name='cnpjsind',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2230infomandsind',
            name='infonusremun',
            field=models.IntegerField(choices=[(1, '1 - Apenas do Empregador'), (2, '2 - Apenas do Sindicato'), (3, '3 - Parte do Empregador, sendo a diferen\xe7a e/ou complementa\xe7\xe3o salarial paga pelo Sindicato')], default=0),
        ),
        migrations.AlterField(
            model_name='s2230infomandsind',
            name='s2230_iniafastamento',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230infomandsind_s2230_iniafastamento', to='s2230.s2230iniAfastamento'),
        ),
        migrations.AlterField(
            model_name='s2230inforetif',
            name='origretif',
            field=models.IntegerField(choices=[(1, '1 - Por iniciativa do empregador'), (2, '2 - Revis\xe3o Administrativa'), (3, '3 - Determina\xe7\xe3o Judicial')], default=0),
        ),
        migrations.AlterField(
            model_name='s2230inforetif',
            name='s2230_evtafasttemp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230inforetif_s2230_evtafasttemp', to='esocial.s2230evtAfastTemp'),
        ),
        migrations.AlterField(
            model_name='s2230iniafastamento',
            name='codmotafast',
            field=models.CharField(choices=[(b'01', '01 - Acidente/Doen\xe7a do trabalho'), (b'03', '03 - Acidente/Doen\xe7a n\xe3o relacionada ao trabalho'), (b'05', '05 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), sem remunera\xe7\xe3o'), (b'06', '06 - Aposentadoria por invalidez'), (b'07', '07 - Acompanhamento - Licen\xe7a para acompanhamento de membro da fam\xedlia enfermo'), (b'08', '08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, \xa76\xba, Dec. 99.684/90 (Regulamento do FGTS)'), (b'10', '10 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), com remunera\xe7\xe3o'), (b'11', '11 - C\xe1rcere'), (b'12', '12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25\xb0, par\xe1grafo \xfanico - Celetistas em geral'), (b'13', '13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1\xb0, inciso II, al\xednea 1 - Servidor p\xfablico, estatut\xe1rio ou n\xe3o, dos \xf3rg\xe3os ou entidades da Administra\xe7\xe3o Direta ou Indireta da Uni\xe3o, dos Estados, do Distrito Federal, dos Muni (...)'), (b'14', '14 - Cess\xe3o / Requisi\xe7\xe3o'), (b'15', '15 - Gozo de f\xe9rias ou recesso - Afastamento tempor\xe1rio para o gozo de f\xe9rias ou recesso'), (b'16', '16 - Licen\xe7a remunerada - Lei, liberalidade da empresa ou Acordo/Conven\xe7\xe3o Coletiva de Trabalho'), (b'17', '17 - Licen\xe7a Maternidade - 120 dias e suas prorroga\xe7\xf5es/antecipa\xe7\xf5es, inclusive para o c\xf4njuge sobrevivente'), (b'18', '18 - Licen\xe7a Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidad\xe3), inclusive para o c\xf4njuge sobrevivente'), (b'19', '19 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de aborto n\xe3o criminoso'), (b'20', '20 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de licen\xe7a-maternidade decorrente de ado\xe7\xe3o ou guarda judicial de crian\xe7a, inclusive para o c\xf4njuge sobrevivente'), (b'21', '21 - Licen\xe7a n\xe3o remunerada ou Sem Vencimento'), (b'22', '22 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, sem remunera\xe7\xe3o'), (b'23', '23 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, com remunera\xe7\xe3o'), (b'24', '24 - Mandato Sindical - Afastamento tempor\xe1rio para exerc\xedcio de mandato sindical'), (b'25', '25 - Mulher v\xedtima de viol\xeancia - Lei 11.340/2006 - art. 9\xba \xa72o, II - Lei Maria da Penha'), (b'26', '26 - Participa\xe7\xe3o de empregado no Conselho Nacional de Previd\xeancia Social-CNPS (art. 3\xba, Lei 8.213/1991)'), (b'27', '27 - Qualifica\xe7\xe3o - Afastamento por suspens\xe3o do contrato de acordo com o art 476-A da CLT'), (b'28', '28 - Representante Sindical - Afastamento pelo tempo que se fizer necess\xe1rio, quando, na qualidade de representante de entidade sindical, estiver participando de reuni\xe3o oficial de organismo internacional do qual o Brasil seja membro'), (b'29', '29 - Servi\xe7o Militar - Afastamento tempor\xe1rio para prestar servi\xe7o militar obrigat\xf3rio;'), (b'30', '30 - Suspens\xe3o disciplinar - CLT, art. 474'), (b'31', '31 - Servidor P\xfablico em Disponibilidade'), (b'33', '33 - Licen\xe7a Maternidade - de 180 dias, Lei 13.301/2016.'), (b'34', '34 - Inatividade do trabalhador avulso (portu\xe1rio ou n\xe3o portu\xe1rio) por per\xedodo superior a 90 dias')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2230iniafastamento',
            name='dtiniafast',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2230iniafastamento',
            name='s2230_evtafasttemp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2230iniafastamento_s2230_evtafasttemp', to='esocial.s2230evtAfastTemp'),
        ),
    ]
