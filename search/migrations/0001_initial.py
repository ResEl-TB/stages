# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recherche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('zone', models.CharField(verbose_name='Zone géographique', choices=[('Île-de-France', 'Île-de-France'), ('Ouest de la France', 'Ouest de la France'), ('Nord de la France', 'Nord de la France'), ('Est de la France', 'Est de la France'), ('Sud de la France', 'Sud de la France'), ('Étranger', 'Étranger')], max_length=20, blank=True)),
                ('ville', models.CharField(verbose_name='Ville', max_length=30, blank=True)),
                ('domain', models.CharField(verbose_name='Domaine concerné', choices=[('Audit / Finance / Gestion', (('Actuariat / Assurance', 'Actuariat / Assurance'), ('Audit', 'Audit'), ('Contrôle de gestion / Comptabilité', 'Contrôle de gestion / Comptabilité'), ("Finance d'entreprise", "Finance d'entreprise"), ('Finance de marché', 'Finance de marché'), ("Gestion d'actif", "Gestion d'actif"))), ('Commercial / Business development', (('Commercial / Business development', 'Commercial / Business development'),)), ('Conseil stratégie', (('Conseil en SI', 'Conseil en SI'), ('Organisation / Transformation', 'Organisation / Transformation'), ('Stratégie / Management', 'Stratégie / Management'))), ('Informatique / SI / Réseaux', (('Développement informatique', 'Développement informatique'), ('Gestion de projet SI', 'Gestion de projet SI'), ('Infrastructure / Réseaux / Télécoms', 'Infrastructure / Réseaux / Télécoms'))), ('Droit / Ressources humaines', (('Juridique / Fiscal', 'Juridique / Fiscal'), ('Ressources humaines', 'Ressources humaines'))), ('Direction / Centre de profit', (('Direction / Centre de profit', 'Direction / Centre de profit'),)), ('Marketing / Communication', (('Marketing / Communication', 'Marketing / Communication'),))], max_length=50, blank=True)),
                ('duree', models.CharField(verbose_name='Durée du contrat', choices=[('1 mois', '1 mois'), ('2 mois', '2 mois'), ('3 mois', '3 mois'), ('4 mois', '4 mois'), ('5 mois', '5 mois'), ('6 mois', '6 mois'), ('Plus de 6 mois', 'Plus de 6 mois')], max_length=20, blank=True)),
                ('type_entreprise', models.CharField(verbose_name="Type d'entreprise", choices=[('PME', 'PME'), ('Grand groupe', 'Grand groupe')], max_length=15, blank=True)),
                ('type_de_contrat', models.CharField(verbose_name='Type de contrat', choices=[('Alternance', 'Alternance'), ('Stage', 'Stage')], max_length=20, blank=True)),
            ],
        ),
    ]
