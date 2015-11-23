# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20151118_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200, verbose_name=b'Nom du domaine')),
            ],
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='domain',
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 22, 29, 43, 548930, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AddField(
            model_name='annonce',
            name='domain',
            field=models.ManyToManyField(to='post.Domaine'),
        ),
    ]
