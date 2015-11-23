# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20151018_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='dates',
        ),
        migrations.AddField(
            model_name='annonce',
            name='date',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'Date de d\xc3\xa9but du contrat'),
        ),
    ]
