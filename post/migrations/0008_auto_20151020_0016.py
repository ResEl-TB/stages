# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20151019_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 22, 16, 42, 288622, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
    ]
