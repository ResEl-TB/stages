# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20150807_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='contact',
            field=models.EmailField(max_length=254, verbose_name=b'Contact'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='dates',
            field=models.CharField(max_length=100, verbose_name=b'Dates de d\xc3\xa9but et de fin du contrat'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='domain',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'Domaine concern\xc3\xa9', choices=[(b'', b''), (b'Audit / Finance / Gestion', ((b'Actuariat / Assurance', b'Actuariat / Assurance'), (b'Audit', b'Audit'), (b'Contr\xc3\xb4le de gestion / Comptabilit\xc3\xa9', b'Contr\xc3\xb4le de gestion / Comptabilit\xc3\xa9'), (b"Finance d'entreprise", b"Finance d'entreprise"), (b'Finance de march\xc3\xa9', b'Finance de march\xc3\xa9'), (b"Gestion d'actif", b"Gestion d'actif"))), (b'Commercial / Business development', ((b'Commercial / Business development', b'Commercial / Business development'),)), (b'Conseil strat\xc3\xa9gie', ((b'Conseil en SI', b'Conseil en SI'), (b'Organisation / Transformation', b'Organisation / Transformation'), (b'Strat\xc3\xa9gie / Management', b'Strat\xc3\xa9gie / Management'))), (b'Informatique / SI / R\xc3\xa9seaux', ((b'D\xc3\xa9veloppement informatique', b'D\xc3\xa9veloppement informatique'), (b'Gestion de projet SI', b'Gestion de projet SI'), (b'Infrastructure / R\xc3\xa9seaux / T\xc3\xa9l\xc3\xa9coms', b'Infrastructure / R\xc3\xa9seaux / T\xc3\xa9l\xc3\xa9coms'))), (b'Droit / Ressources humaines', ((b'Juridique / Fiscal', b'Juridique / Fiscal'), (b'Ressources humaines', b'Ressources humaines'))), (b'Direction / Centre de profit', ((b'Direction / Centre de profit', b'Direction / Centre de profit'),)), (b'Marketing / Communication', ((b'Marketing / Communication', b'Marketing / Communication'),))]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='duree',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'Dur\xc3\xa9e du contrat', choices=[(b'', b''), (b'1 mois', b'1 mois'), (b'2 mois', b'2 mois'), (b'3 mois', b'3 mois'), (b'4 mois', b'4 mois'), (b'5 mois', b'5 mois'), (b'6 mois', b'6 mois'), (b'Plus de 6 mois', b'Plus de 6 mois')]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='keywords',
            field=models.CharField(help_text=b'Pas plus de 3', max_length=40, verbose_name=b'Mots-cl\xc3\xa9'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_de_contrat',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'Type de contrat', choices=[(b'', b''), (b'Alternance', b'Alternance'), (b'Stage', b'Stage')]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_entreprise',
            field=models.CharField(default=b'', max_length=15, verbose_name=b"Type d'entreprise", choices=[(b'', b''), (b'PME', b'PME'), (b'Grand groupe', b'Grand groupe')]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='ville',
            field=models.CharField(help_text=b'Ville o\xc3\xb9 se d\xc3\xa9roule le contrat', max_length=30, verbose_name=b'Ville'),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='zone',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'Zone g\xc3\xa9ographique', choices=[(b'', b''), (b'\xc3\x8ele-de-France', b'\xc3\x8ele-de-France'), (b'Ouest de la France', b'Ouest de la France'), (b'Nord de la France', b'Nord de la France'), (b'Est de la France', b'Est de la France'), (b'Sud de la France', b'Sud de la France'), (b'\xc3\x89tranger', b'\xc3\x89tranger')]),
        ),
        migrations.AlterField(
            model_name='modo',
            name='annonce',
            field=models.TextField(verbose_name=b'D\xc3\xa9posez votre annonce ici'),
        ),
    ]
