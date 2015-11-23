# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20151118_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='domain',
            field=models.ManyToManyField(to='post.Domaine', verbose_name='Domaine concern\xe9'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 23, 1, 14, 162290, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
    ]
