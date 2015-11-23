# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20151020_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recherche',
            name='type_entreprise',
            field=models.CharField(blank=True, max_length=15, verbose_name=b"Type d'entreprise", choices=[(b'Microentreprise', b'Microentreprise (moins de 10 employ\xc3\xa9s)'), (b'PME', b'PME (entre 10 et 250 emply\xc3\xa9s)'), (b'Grand groupe', b'Grand groupe')]),
        ),
    ]
