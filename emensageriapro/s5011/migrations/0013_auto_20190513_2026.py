# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0012_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5011infoemprparcial',
            options={'managed': True, 'ordering': ['s5011_idelotacao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop', 'cnoobra'], 'permissions': (('can_view_s5011_infoemprparcial', 'Can view s5011_infoemprparcial'),)},
        ),
        migrations.AddField(
            model_name='s5011infoemprparcial',
            name='cnoobra',
            field=models.CharField(default=b'A', max_length=12),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='indaquis',
            field=models.IntegerField(choices=[(1, '1 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral'), (2, '2 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA'), (3, '3 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA'), (4, '4 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (5, '5 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (6, '6 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018). Evento de origem (S-1250).')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='s5011_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011basesaquis_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vlraquis',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrcpcalcpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrcpnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrratcalcpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrratnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrsenarcalc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='vrsenarnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='s5011_idelotacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011basesavnport_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrbccp00',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrbccp13',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrbccp15',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrbccp20',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrbccp25',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrbcfgts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='vrdesccp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='indcomerc',
            field=models.IntegerField(choices=[(2, '2 - Comercializa\xe7\xe3o da Produ\xe7\xe3o efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa f\xedsica por Produtor Rural Pessoa F\xedsica, inclusive por Segurado Especial ou por Pessoa F\xedsica n\xe3o produtor rural'), (3, '3 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PF/Seg. Especial - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA) ou a Intermedi\xe1rio PF'), (7, '7 - Comercializa\xe7\xe3o da Produ\xe7\xe3o Isenta de acordo com a Lei n\xb0 13.606/2018'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o da Pessoa F\xedsica/Segurado Especial para Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o da Produ\xe7\xe3o no Mercado Externo. Origem: {indComerc} do S-1260.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='s5011_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011basescomerc_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='vrbccompr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='vrcpsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='vrratsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='vrsenarsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='codcateg',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='indincid',
            field=models.IntegerField(choices=[(1, '1 - Normal'), (2, '2 - Ativ. Concomitante'), (9, '9 - Substitu\xedda ou Isenta.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='s5011_idelotacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011basesremun_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrbccp00',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrbccp15',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrbccp20',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrbccp25',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrcalcsenat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrcalcsest',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrdescsenat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrdescsest',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrsalfam',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrsalmat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrsuspbccp00',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrsuspbccp15',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrsuspbccp20',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='vrsuspbccp25',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='aliqrat',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='aliqratajust',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='cnpjopportuario',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='fap',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='s5011_idelotacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011dadosopport_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=15),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='s5011_evtcs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011ideestab_s5011_evtcs', to='esocial.s5011evtCS'),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='codlotacao',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='codtercs',
            field=models.CharField(choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], default=b'A', max_length=4),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='codtercssusp',
            field=models.CharField(blank=True, choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='fpas',
            field=models.IntegerField(choices=[(507, '507 - 507'), (515, '515 - 515'), (523, '523 - 523'), (531, '531 - 531'), (540, '540 - 540'), (558, '558 - 558'), (566, '566 - 566'), (574, '574 - 574'), (582, '582 - 582'), (590, '590 - 590'), (604, '604 - 604'), (612, '612 - 612'), (620, '620 - 620'), (639, '639 - 639'), (647, '647 - 647'), (655, '655 - 655'), (680, '680 - 680'), (736, '736 - 736'), (744, '744 - 744'), (779, '779 - 779'), (787, '787 - 787'), (795, '795 - 795'), (825, '825 - 825'), (833, '833 - 833'), (868, '868 - 868'), (876, '876 - 876')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='s5011_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011idelotacao_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
        migrations.AlterField(
            model_name='s5011infoatconc',
            name='fator13',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infoatconc',
            name='fatormes',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infoatconc',
            name='s5011_infopj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infoatconc_s5011_infopj', to='s5011.s5011infoPJ'),
        ),
        migrations.AlterField(
            model_name='s5011infocomplobra',
            name='indsubstpatrobra',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Patronal Substitu\xedda'), (2, '2 - Contribui\xe7\xe3o Patronal N\xe3o Substitu\xedda.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011infocomplobra',
            name='s5011_infoestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infocomplobra_s5011_infoestab', to='s5011.s5011infoEstab'),
        ),
        migrations.AlterField(
            model_name='s5011infocpseg',
            name='s5011_evtcs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infocpseg_s5011_evtcs', to='esocial.s5011evtCS'),
        ),
        migrations.AlterField(
            model_name='s5011infocpseg',
            name='vrcpseg',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infocpseg',
            name='vrdesccp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='s5011_evtcs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infocrcontrib_s5011_evtcs', to='esocial.s5011evtCS'),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='tpcr',
            field=models.CharField(default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='vrcr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='vrcrsusp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='s5011_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infocrestab_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='tpcr',
            field=models.CharField(default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='vrcr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='vrsuspcr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='nrinsccontrat',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='nrinscprop',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='s5011_idelotacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infoemprparcial_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='tpinsccontrat',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='tpinscprop',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='aliqrat',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='aliqratajust',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='cnaeprep',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='fap',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='s5011_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infoestab_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='indconstr',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o \xe9 Construtora'), (1, '1 - Empresa Construtora. Evento de origem (S-1000).')], default=0),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='indcoop',
            field=models.IntegerField(blank=True, choices=[(0, '0 - N\xe3o \xe9 cooperativa'), (1, '1 - Cooperativa de Trabalho'), (2, '2 - Cooperativa de Produ\xe7\xe3o'), (3, '3 - Outras Cooperativas. Evento de origem (S-1000).')], null=True),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='indsubstpatr',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Integralmente substitu\xedda'), (2, '2 - Parcialmente substitu\xedda. Origem: {indSubsPatr} de S-1280.')], null=True),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='percredcontrib',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='s5011_evtcs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infopj_s5011_evtcs', to='esocial.s5011evtCS'),
        ),
        migrations.AlterField(
            model_name='s5011infosubstpatropport',
            name='cnpjopportuario',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s5011infosubstpatropport',
            name='s5011_idelotacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infosubstpatropport_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AlterField(
            model_name='s5011infotercsusp',
            name='codterc',
            field=models.CharField(choices=[(b'507', '507 - 507'), (b'515', '515 - 515'), (b'523', '523 - 523'), (b'531', '531 - 531'), (b'540', '540 - 540'), (b'558', '558 - 558'), (b'566', '566 - 566'), (b'574', '574 - 574'), (b'582', '582 - 582'), (b'590', '590 - 590'), (b'604', '604 - 604'), (b'612', '612 - 612'), (b'620', '620 - 620'), (b'639', '639 - 639'), (b'647', '647 - 647'), (b'655', '655 - 655'), (b'680', '680 - 680'), (b'736', '736 - 736'), (b'744', '744 - 744'), (b'779', '779 - 779'), (b'787', '787 - 787'), (b'795', '795 - 795'), (b'825', '825 - 825'), (b'833', '833 - 833'), (b'868', '868 - 868'), (b'876', '876 - 876')], default=b'A', max_length=4),
        ),
        migrations.AlterField(
            model_name='s5011infotercsusp',
            name='s5011_idelotacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5011infotercsusp_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
    ]
