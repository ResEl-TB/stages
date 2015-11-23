# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20151120_0945'),
        ('search', '0006_auto_20151118_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recherchefields',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='recherchefields',
            name='ville',
        ),
        migrations.RemoveField(
            model_name='recherchefields',
            name='domain',
        ),
        migrations.AddField(
            model_name='recherchefields',
            name='domain',
            field=models.ManyToManyField(to='post.Domaine', verbose_name='Domaine concern\xe9', blank=True),
        ),
    ]
