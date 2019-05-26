# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1300', '0011_auto_20190513_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1300contribsind',
            name='cnpjsindic',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s1300contribsind',
            name='s1300_evtcontrsindpatr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1300contribsind_s1300_evtcontrsindpatr', to='esocial.s1300evtContrSindPatr'),
        ),
        migrations.AlterField(
            model_name='s1300contribsind',
            name='tpcontribsind',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Sindical Compuls\xf3ria'), (2, '2 - Contribui\xe7\xe3o Associativa'), (3, '3 - Contribui\xe7\xe3o Assistencial'), (4, '4 - Contribui\xe7\xe3o Confederativa.')]),
        ),
        migrations.AlterField(
            model_name='s1300contribsind',
            name='vlrcontribsind',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
