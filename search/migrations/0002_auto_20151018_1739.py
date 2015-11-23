# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recherche',
            name='domain',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'Domaine concern\xc3\xa9', choices=[(b'Audit / Finance / Gestion', ((b'Actuariat / Assurance', b'Actuariat / Assurance'), (b'Audit', b'Audit'), (b'Contr\xc3\xb4le de gestion / Comptabilit\xc3\xa9', b'Contr\xc3\xb4le de gestion / Comptabilit\xc3\xa9'), (b"Finance d'entreprise", b"Finance d'entreprise"), (b'Finance de march\xc3\xa9', b'Finance de march\xc3\xa9'), (b"Gestion d'actif", b"Gestion d'actif"))), (b'Commercial / Business development', ((b'Commercial / Business development', b'Commercial / Business development'),)), (b'Conseil strat\xc3\xa9gie', ((b'Conseil en SI', b'Conseil en SI'), (b'Organisation / Transformation', b'Organisation / Transformation'), (b'Strat\xc3\xa9gie / Management', b'Strat\xc3\xa9gie / Management'))), (b'Informatique / SI / R\xc3\xa9seaux', ((b'D\xc3\xa9veloppement informatique', b'D\xc3\xa9veloppement informatique'), (b'Gestion de projet SI', b'Gestion de projet SI'), (b'Infrastructure / R\xc3\xa9seaux / T\xc3\xa9l\xc3\xa9coms', b'Infrastructure / R\xc3\xa9seaux / T\xc3\xa9l\xc3\xa9coms'))), (b'Droit / Ressources humaines', ((b'Juridique / Fiscal', b'Juridique / Fiscal'), (b'Ressources humaines', b'Ressources humaines'))), (b'Direction / Centre de profit', ((b'Direction / Centre de profit', b'Direction / Centre de profit'),)), (b'Marketing / Communication', ((b'Marketing / Communication', b'Marketing / Communication'),))]),
        ),
        migrations.AlterField(
            model_name='recherche',
            name='duree',
            field=models.CharField(blank=True, max_length=20, verbose_name=b'Dur\xc3\xa9e du contrat', choices=[(b'1 mois', b'1 mois'), (b'2 mois', b'2 mois'), (b'3 mois', b'3 mois'), (b'4 mois', b'4 mois'), (b'5 mois', b'5 mois'), (b'6 mois', b'6 mois'), (b'Plus de 6 mois', b'Plus de 6 mois')]),
        ),
        migrations.AlterField(
            model_name='recherche',
            name='zone',
            field=models.CharField(blank=True, max_length=20, verbose_name=b'Zone g\xc3\xa9ographique', choices=[(b'\xc3\x8ele-de-France', b'\xc3\x8ele-de-France'), (b'Ouest de la France', b'Ouest de la France'), (b'Nord de la France', b'Nord de la France'), (b'Est de la France', b'Est de la France'), (b'Sud de la France', b'Sud de la France'), (b'\xc3\x89tranger', b'\xc3\x89tranger')]),
        ),
    ]
