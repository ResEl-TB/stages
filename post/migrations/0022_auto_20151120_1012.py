# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20151120_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duree', models.CharField(max_length=50, verbose_name=b'Dur\xc3\xa9e du contrat')),
            ],
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_organisme', models.CharField(max_length=100, verbose_name=b"Type d'organisme")),
            ],
        ),
        migrations.CreateModel(
            name='TypeContrat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_contrat', models.CharField(max_length=100, verbose_name=b'Nature du contrat')),
            ],
        ),
        migrations.AlterField(
            model_name='annonce',
            name='commentaires',
            field=models.TextField(verbose_name=b"Commentaires \xc3\xa0 propos de l'annonce", blank=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='date_debut',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'Date de d\xc3\xa9but du contrat', blank=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='domain',
            field=models.ManyToManyField(to='post.Domaine', verbose_name=b'Domaine concern\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='duree',
            field=models.OneToOneField(verbose_name=b'Dur\xc3\xa9e du contrat', to='post.Duree'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 9, 12, 27, 143294, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_de_contrat',
            field=models.OneToOneField(verbose_name=b'Type de contrat', to='post.TypeContrat'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_organisme',
            field=models.OneToOneField(verbose_name=b"Type d'organisme", blank=True, to='post.Organisme'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='ville',
            field=models.CharField(help_text=b'Ville o\xc3\xb9 se d\xc3\xa9roule le contrat', max_length=30, verbose_name=b'Ville', blank=True),
        ),
    ]
