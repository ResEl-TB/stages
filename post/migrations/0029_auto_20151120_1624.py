# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_auto_20151120_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annonce',
            old_name='fichiers',
            new_name='fichier',
        ),
        migrations.AddField(
            model_name='annonce',
            name='multiple_files',
            field=models.BooleanField(default=None, verbose_name=b'Le fichier contient plusieurs annonces ?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='annonce',
            name='domain',
            field=models.ManyToManyField(help_text=b'Maintenir la touche Ctrl pour choisir plusieurs domaines', to='post.Domaine', verbose_name=b'Domaine concern\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 15, 23, 12, 925075, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
    ]
