# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20151018_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='recherche',
            name='date',
            field=models.CharField(max_length=10, verbose_name=b'D\xc3\xa9but du contrat', blank=True),
        ),
    ]
