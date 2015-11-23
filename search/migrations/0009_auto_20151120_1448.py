# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20151120_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recherchefields',
            name='duree',
            field=models.ForeignKey(verbose_name=b'Dur\xc3\xa9e du contrat', blank=True, to='post.Duree'),
        ),
        migrations.AlterField(
            model_name='recherchefields',
            name='type_de_contrat',
            field=models.ForeignKey(verbose_name=b'Nature du contrat', blank=True, to='post.TypeContrat'),
        ),
        migrations.AlterField(
            model_name='recherchefields',
            name='zone',
            field=models.ForeignKey(verbose_name=b'Zone g\xc3\xa9ographique', blank=True, to='post.Zone'),
        ),
    ]
