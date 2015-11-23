# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20151120_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 9, 38, 12, 471573, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_organisme',
            field=models.OneToOneField(null=True, blank=True, to='post.Organisme', verbose_name=b"Type d'organisme"),
        ),
    ]
