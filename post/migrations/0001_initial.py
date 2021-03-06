# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import post.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(blank=True, max_length=30, verbose_name='Ville')),
                ('date_debut', models.CharField(blank=True, default='', max_length=10, verbose_name='Date de début du contrat')),
                ('nom_entreprise', models.CharField(max_length=40, verbose_name="Nom de l'entreprise")),
                ('fichier', models.FileField(blank=True, default='', upload_to='annonces/%Y/%m/%d', validators=[post.validators.validate_file_extension], verbose_name="Fichier contenant l'annonce")),
                ('multiple_files', models.CharField(choices=[('1', 'Oui'), ('0', 'Non')], default='0', max_length=1, verbose_name='Le fichier contient plusieurs annonces ?')),
                ('url_annonce', models.URLField(blank=True, default='', verbose_name="URL vers l'annonce")),
                ('commentaires', models.TextField(blank=True, verbose_name="Commentaires à propos de l'annonce")),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('visites', models.IntegerField(default=0, editable=False, verbose_name='Visites')),
            ],
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom du domaine')),
            ],
        ),
        migrations.CreateModel(
            name='Duree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree', models.CharField(max_length=50, verbose_name='Durée du contrat')),
            ],
            options={
                'verbose_name': 'durée',
            },
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_organisme', models.CharField(max_length=100, null=True, verbose_name="Type d'organisme")),
            ],
        ),
        migrations.CreateModel(
            name='TypeContrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contrat', models.CharField(max_length=100, verbose_name='Nature du contrat')),
            ],
            options={
                'verbose_name': 'type de contrat',
                'verbose_name_plural': 'types de contrat',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Zone géographique du stage')),
            ],
            options={
                'verbose_name': 'zone géographique',
                'verbose_name_plural': 'zones géographique',
            },
        ),
        migrations.AddField(
            model_name='annonce',
            name='domain',
            field=models.ManyToManyField(help_text='Maintenir la touche Ctrl pour choisir plusieurs domaines', to='post.Domaine', verbose_name='Domaine concerné'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='duree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Duree', verbose_name='Durée du contrat'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='type_de_contrat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.TypeContrat', verbose_name='Type de contrat'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='type_organisme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Organisme', verbose_name="Type d'organisme"),
        ),
        migrations.AddField(
            model_name='annonce',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Zone', verbose_name="Localisation de l'annonce"),
        ),
    ]
