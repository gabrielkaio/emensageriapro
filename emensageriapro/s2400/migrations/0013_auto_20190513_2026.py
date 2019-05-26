# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2400', '0012_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2400brasil',
            name='cep',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='codmunic',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=80),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='nrlograd',
            field=models.CharField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='s2400_endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2400brasil_s2400_endereco', to='s2400.s2400endereco'),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='tplograd',
            field=models.TextField(default=b'A'),
        ),
        migrations.AlterField(
            model_name='s2400brasil',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='depfinsprev',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='depirrf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='dtnascto',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='incfismen',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='nmdep',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='s2400_evtcdbenefin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2400dependente_s2400_evtcdbenefin', to='esocial.s2400evtCdBenefIn'),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='sexodep',
            field=models.CharField(choices=[(b'F', 'F - Feminino.'), (b'M', 'M - Masculino')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2400dependente',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2400endereco',
            name='s2400_evtcdbenefin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2400endereco_s2400_evtcdbenefin', to='esocial.s2400evtCdBenefIn'),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=80),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='nmcid',
            field=models.CharField(default=b'A', max_length=50),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='nrlograd',
            field=models.CharField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='paisresid',
            field=models.TextField(default=b'A'),
        ),
        migrations.AlterField(
            model_name='s2400exterior',
            name='s2400_endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2400exterior_s2400_endereco', to='s2400.s2400endereco'),
        ),
    ]
