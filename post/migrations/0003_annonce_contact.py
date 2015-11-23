# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150806_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='contact',
            field=models.EmailField(verbose_name='Contact', max_length=254, default='exemple@exemple.com'),
        ),
    ]
