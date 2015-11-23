# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20151020_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 20, 15, 48, 1, 981754, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
    ]
