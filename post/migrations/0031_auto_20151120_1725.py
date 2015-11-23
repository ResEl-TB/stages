# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0030_auto_20151120_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 16, 25, 12, 286758, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='ville',
            field=models.CharField(max_length=30, verbose_name=b'Ville', blank=True),
        ),
    ]
