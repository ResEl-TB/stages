# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20151118_1645'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Modo',
        ),
        migrations.AlterField(
            model_name='annonce',
            name='fichiers',
            field=models.FileField(default=b'', upload_to=b'annonces/%Y/%m/%d', verbose_name=b"Fichier contenant l'annonce", blank=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 22, 15, 1, 41760, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='url_annonce',
            field=models.URLField(default=b'', verbose_name=b"URL vers l'annonce", blank=True),
        ),
    ]
