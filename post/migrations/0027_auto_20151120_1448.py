# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_auto_20151120_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='duree',
            field=models.ForeignKey(verbose_name=b'Dur\xc3\xa9e du contrat', to='post.Duree'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 13, 48, 5, 278642, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_de_contrat',
            field=models.ForeignKey(verbose_name=b'Type de contrat', to='post.TypeContrat'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_organisme',
            field=models.ForeignKey(verbose_name=b"Type d'organisme", blank=True, to='post.Organisme', null=True),
        ),
    ]
