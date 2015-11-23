# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import post.validators
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_auto_20151118_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='fichiers',
            field=models.FileField(default=b'', validators=[post.validators.validate_file_extension], upload_to=b'annonces/%Y/%m/%d', blank=True, verbose_name=b"Fichier contenant l'annonce"),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 22, 57, 30, 757335, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
    ]
