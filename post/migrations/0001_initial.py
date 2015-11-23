# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('zone', models.CharField(choices=[('Île-de-France', 'Île-de-France'), ('Ouest de la France', 'Ouest de la France'), ('Nord de la France', 'Nord de la France'), ('Est de la France', 'Est de la France'), ('Sud de la France', 'Sud de la France'), ('Étranger', 'Étranger')], max_length=20, verbose_name='Zone géographique')),
                ('ville', models.CharField(max_length=30, verbose_name='Ville')),
                ('domain', models.CharField(choices=[('Audit / Finance / Gestion', (('Actuariat / Assurance', 'Actuariat / Assurance'), ('Audit', 'Audit'), ('Contrôle de gestion / Comptabilité', 'Contrôle de gestion / Comptabilité'), ("Finance d'entreprise", "Finance d'entreprise"), ('Finance de marché', 'Finance de marché'), ("Gestion d'actif", "Gestion d'actif"))), ('Commercial / Business development', (('Commercial / Business development', 'Commercial / Business development'),)), ('Conseil stratégie', (('Conseil en SI', 'Conseil en SI'), ('Organisation / Transformation', 'Organisation / Transformation'), ('Stratégie / Management', 'Stratégie / Management'))), ('Informatique / SI / Réseaux', (('Développement informatique', 'Développement informatique'), ('Gestion de projet SI', 'Gestion de projet SI'), ('Infrastructure / Réseaux / Télécoms', 'Infrastructure / Réseaux / Télécoms'))), ('Droit / Ressources humaines', (('Juridique / Fiscal', 'Juridique / Fiscal'), ('Ressources humaines', 'Ressources humaines'))), ('Direction / Centre de profit', (('Direction / Centre de profit', 'Direction / Centre de profit'),)), ('Marketing / Communication', (('Marketing / Communication', 'Marketing / Communication'),))], max_length=50, verbose_name='Domaine concerné')),
                ('duree', models.CharField(choices=[('1 mois', '1 mois'), ('2 mois', '2 mois'), ('3 mois', '3 mois'), ('4 mois', '4 mois'), ('5 mois', '5 mois'), ('6 mois', '6 mois'), ('Plus de 6 mois', 'Plus de 6 mois')], max_length=20, verbose_name='Durée du contrat')),
                ('type_entreprise', models.CharField(choices=[('PME', 'PME'), ('Grand groupe', 'Grand groupe')], max_length=15, verbose_name="Type d'entreprise")),
                ('nom_entreprise', models.CharField(max_length=40, verbose_name="Nom de l'entreprise")),
                ('type_de_contrat', models.CharField(choices=[('Alternance', 'Alternance'), ('Stage', 'Stage')], max_length=20, verbose_name='Type de contrat')),
                ('description', models.TextField(verbose_name="Description de l'annonce")),
                ('keywords', models.CharField(max_length=40, help_text='~ Pas plus de 3, séparés par des espaces ~', verbose_name='Mots-clé')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 7, 12, 20, 11, 34, 116020, tzinfo=utc), verbose_name='Date de publication', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Modo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('annonce', models.TextField(verbose_name='Déposez votre annonce ici')),
            ],
        ),
    ]
