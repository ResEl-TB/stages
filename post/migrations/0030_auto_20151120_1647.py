# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_auto_20151120_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='multiple_files',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'Le fichier contient plusieurs annonces ?', choices=[(b'1', b'Oui'), (b'0', b'Non')]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 15, 47, 49, 511891, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
    ]
