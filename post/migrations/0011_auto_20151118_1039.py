# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20151020_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 9, 39, 21, 866608, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_entreprise',
            field=models.CharField(default=b'', max_length=15, verbose_name=b"Type d'entreprise", choices=[(b'', b''), (b'Microentreprise', b'Microentreprise (moins de 10 employ\xc3\xa9s)'), (b'PME', b'PME (entre 10 et 250 employ\xc3\xa9s)'), (b'Grand groupe', b'Grand groupe')]),
        ),
    ]
