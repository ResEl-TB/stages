# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_auto_20151120_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='recherchefields',
            name='nom_entreprise',
            field=models.CharField(max_length=40, verbose_name=b"Nom de l'entreprise", blank=True),
        ),
    ]
