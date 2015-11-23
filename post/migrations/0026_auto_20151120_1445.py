# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_auto_20151120_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 13, 45, 44, 18967, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='zone',
            field=models.ForeignKey(verbose_name=b"Localisation de l'annonce", to='post.Zone'),
        ),
    ]
