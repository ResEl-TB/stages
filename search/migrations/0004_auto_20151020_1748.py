# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_recherche_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recherche',
            name='keywords',
            field=models.CharField(max_length=100, verbose_name=b'Mots-cl\xc3\xa9', blank=True),
        ),
        migrations.AlterField(
            model_name='recherche',
            name='date',
            field=models.CharField(max_length=7, verbose_name=b'D\xc3\xa9but du contrat', blank=True),
        ),
    ]
