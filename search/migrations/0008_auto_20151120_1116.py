# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20151120_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recherchefields',
            name='type_organisme',
        ),
        migrations.AlterField(
            model_name='recherchefields',
            name='domain',
            field=models.ManyToManyField(to='post.Domaine', verbose_name=b'Domaine concern\xc3\xa9', blank=True),
        ),
        migrations.AlterField(
            model_name='recherchefields',
            name='duree',
            field=models.OneToOneField(verbose_name=b'Dur\xc3\xa9e du contrat', blank=True, to='post.Duree'),
        ),
        migrations.AlterField(
            model_name='recherchefields',
            name='type_de_contrat',
            field=models.OneToOneField(verbose_name=b'Nature du contrat', blank=True, to='post.TypeContrat'),
        ),
        migrations.AlterField(
            model_name='recherchefields',
            name='zone',
            field=models.OneToOneField(verbose_name=b'Zone g\xc3\xa9ographique', blank=True, to='post.Zone'),
        ),
    ]
