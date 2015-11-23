# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_annonce_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='dates',
            field=models.CharField(verbose_name='Dates de début et de fin du contrat', max_length=100, default='Début - Fin'),
        ),
    ]
