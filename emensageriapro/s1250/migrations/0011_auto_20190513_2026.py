# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1250', '0010_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='indopccp',
            field=models.IntegerField(choices=[(1, '1 - Sobre a comercializa\xe7\xe3o da sua produ\xe7\xe3o'), (2, '2 - Sobre a folha de pagamento.')], default=0),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='nrinscprod',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='s1250_tpaquis',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250ideprodutor_s1250_tpaquis', to='s1250.s1250tpAquis'),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='tpinscprod',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250ideprodutor',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='codsusp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='nrprocjud',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='s1250_tpaquis',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250infoprocj_s1250_tpaquis', to='s1250.s1250tpAquis'),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='vrcpnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='vrratnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250infoprocj',
            name='vrsenarnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='codsusp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='nrprocjud',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='s1250_ideprodutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250infoprocjud_s1250_ideprodutor', to='s1250.s1250ideProdutor'),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='vrcpnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='vrratnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250infoprocjud',
            name='vrsenarnret',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='dtemisnf',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='nrdocto',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='s1250_ideprodutor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250nfs_s1250_ideprodutor', to='s1250.s1250ideProdutor'),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vrcpdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vrratdescpr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250nfs',
            name='vrsenardesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='indaquis',
            field=models.IntegerField(choices=[(1, '1 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral'), (2, '2 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA'), (3, '3 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA'), (4, '4 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (5, '5 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (6, '6 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018).')], default=0),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='s1250_evtaqprod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1250tpaquis_s1250_evtaqprod', to='esocial.s1250evtAqProd'),
        ),
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='vlrtotaquis',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]