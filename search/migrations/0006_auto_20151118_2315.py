# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20151118_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='RechercheFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone', models.CharField(default=b'', max_length=200, verbose_name=b'Zone g\xc3\xa9ographique', blank=True, choices=[(b'', b''), ('\xcele-de-France', '\xcele-de-France'), ('Ouest de la France', 'Ouest de la France'), ('Nord de la France', 'Nord de la France'), ('Est de la France', 'Est de la France'), ('Sud de la France', 'Sud de la France'), ('Toute la France', 'Toute la France'), ('\xc9tranger', '\xc9tranger')])),
                ('ville', models.CharField(default=b'', help_text='Ville o\xf9 se d\xe9roule le contrat', max_length=30, verbose_name=b'Ville', blank=True)),
                ('domain', models.CharField(default=b'', max_length=200, verbose_name='Domaine concern\xe9', blank=True, choices=[(b'', b''), (b'Audit / Finance / Gestion', ((b'Actuariat / Assurance', b'Actuariat / Assurance'), (b'Audit', b'Audit'), ('Contr\xf4le de gestion / Comptabilit\xe9', 'Contr\xf4le de gestion / Comptabilit\xe9'), (b"Finance d'entreprise", b"Finance d'entreprise"), ('Finance de march\xe9', b'Finance de march\xc3\xa9'), (b"Gestion d'actif", b"Gestion d'actif"))), (b'Commercial / Business development', ((b'Commercial / Business development', b'Commercial / Business development'),)), ('Conseil strat\xe9gie', ((b'Conseil en SI', b'Conseil en SI'), (b'Organisation / Transformation', b'Organisation / Transformation'), ('Strat\xe9gie / Management', 'Strat\xe9gie / Management'))), ('Informatique / SI / R\xe9seaux', (('D\xe9veloppement informatique', 'D\xe9veloppement informatique'), (b'Gestion de projet SI', b'Gestion de projet SI'), ('Infrastructure / R\xe9seaux / T\xe9l\xe9coms', 'Infrastructure / R\xe9seaux / T\xe9l\xe9coms'))), (b'Droit / Ressources humaines', ((b'Juridique / Fiscal', b'Juridique / Fiscal'), (b'Ressources humaines', b'Ressources humaines'))), (b'Direction / Centre de profit', ((b'Direction / Centre de profit', b'Direction / Centre de profit'),)), (b'Marketing / Communication', ((b'Marketing / Communication', b'Marketing / Communication'),))])),
                ('date_debut', models.CharField(default=b'', max_length=10, verbose_name='Date de d\xe9but du contrat', blank=True)),
                ('duree', models.CharField(default=b'', max_length=200, verbose_name='Dur\xe9e du contrat', blank=True, choices=[(b'', b''), (b'1 mois', b'1 mois'), (b'2 mois', b'2 mois'), (b'3 mois', b'3 mois'), (b'4 mois', b'4 mois'), (b'5 mois', b'5 mois'), (b'6 mois', b'6 mois'), (b'Plus de 6 mois', b'Plus de 6 mois')])),
                ('type_organisme', models.CharField(default=b'', max_length=200, verbose_name=b"Type d'organisme", blank=True, choices=[(b'', b''), (b'Microentreprise', b'Microentreprise (moins de 10 employ\xc3\xa9s)'), (b'PME', b'PME (entre 10 et 250 employ\xc3\xa9s)'), (b'Grand groupe', b'Grand groupe'), (b'Laboratoire', b'Laboratoire'), (b'Associatif', b'Associatif')])),
                ('type_de_contrat', models.CharField(default=b'', max_length=20, verbose_name=b'Type de contrat', blank=True, choices=[(b'Alternance', b'Alternance'), (b'Stage', b'Stage')])),
            ],
        ),
        migrations.DeleteModel(
            name='Recherche',
        ),
    ]
