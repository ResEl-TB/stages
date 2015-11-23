# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20151120_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50, verbose_name=b'Zone g\xc3\xa9ographique du stage')),
            ],
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 8, 54, 20, 889662, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='zone',
            field=models.OneToOneField(verbose_name=b"Localisation de l'annonce", to='post.Zone'),
        ),
    ]
