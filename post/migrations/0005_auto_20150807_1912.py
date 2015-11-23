# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_annonce_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='keywords',
            field=models.CharField(max_length=40, verbose_name='Mots-clé'),
        ),
    ]
