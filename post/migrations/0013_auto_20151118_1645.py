# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20151118_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='date',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='description',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='type_entreprise',
        ),
        migrations.AddField(
            model_name='annonce',
            name='commentaires',
            field=models.TextField(verbose_name="Commentaires \xe0 propos de l'annonce", blank=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='date_debut',
            field=models.CharField(default=b'', max_length=10, verbose_name='Date de d\xe9but du contrat', blank=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='fichiers',
            field=models.FileField(upload_to=b'annonces/%Y/%m/%d', verbose_name=b"Fichier contenant l'annonce", blank=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='type_organisme',
            field=models.CharField(blank=True, max_length=200, verbose_name=b"Type d'organisme", choices=[(b'', b''), (b'Microentreprise', b'Microentreprise (moins de 10 employ\xc3\xa9s)'), (b'PME', b'PME (entre 10 et 250 employ\xc3\xa9s)'), (b'Grand groupe', b'Grand groupe'), (b'Laboratoire', b'Laboratoire'), (b'Associatif', b'Associatif')]),
        ),
        migrations.AddField(
            model_name='annonce',
            name='url_annonce',
            field=models.URLField(verbose_name=b"URL vers l'annonce", blank=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='domain',
            field=models.CharField(default=b'Audit', max_length=200, verbose_name='Domaine concern\xe9', choices=[(b'Audit / Finance / Gestion', ((b'Actuariat / Assurance', b'Actuariat / Assurance'), (b'Audit', b'Audit'), ('Contr\xf4le de gestion / Comptabilit\xe9', 'Contr\xf4le de gestion / Comptabilit\xe9'), (b"Finance d'entreprise", b"Finance d'entreprise"), ('Finance de march\xe9', b'Finance de march\xc3\xa9'), (b"Gestion d'actif", b"Gestion d'actif"))), (b'Commercial / Business development', ((b'Commercial / Business development', b'Commercial / Business development'),)), ('Conseil strat\xe9gie', ((b'Conseil en SI', b'Conseil en SI'), (b'Organisation / Transformation', b'Organisation / Transformation'), ('Strat\xe9gie / Management', 'Strat\xe9gie / Management'))), ('Informatique / SI / R\xe9seaux', (('D\xe9veloppement informatique', 'D\xe9veloppement informatique'), (b'Gestion de projet SI', b'Gestion de projet SI'), ('Infrastructure / R\xe9seaux / T\xe9l\xe9coms', 'Infrastructure / R\xe9seaux / T\xe9l\xe9coms'))), (b'Droit / Ressources humaines', ((b'Juridique / Fiscal', b'Juridique / Fiscal'), (b'Ressources humaines', b'Ressources humaines'))), (b'Direction / Centre de profit', ((b'Direction / Centre de profit', b'Direction / Centre de profit'),)), (b'Marketing / Communication', ((b'Marketing / Communication', b'Marketing / Communication'),))]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='duree',
            field=models.CharField(default=b'1 mois', max_length=200, verbose_name='Dur\xe9e du contrat', choices=[(b'1 mois', b'1 mois'), (b'2 mois', b'2 mois'), (b'3 mois', b'3 mois'), (b'4 mois', b'4 mois'), (b'5 mois', b'5 mois'), (b'6 mois', b'6 mois'), (b'Plus de 6 mois', b'Plus de 6 mois')]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 15, 45, 1, 458181, tzinfo=utc), verbose_name=b'Date de publication', editable=False),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='type_de_contrat',
            field=models.CharField(default=b'Alternance', max_length=20, verbose_name=b'Type de contrat', choices=[(b'Alternance', b'Alternance'), (b'Stage', b'Stage')]),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='ville',
            field=models.CharField(help_text='Ville o\xf9 se d\xe9roule le contrat', max_length=30, verbose_name=b'Ville', blank=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='zone',
            field=models.CharField(default='Toute la France', max_length=200, verbose_name=b'Zone g\xc3\xa9ographique', choices=[('\xcele-de-France', '\xcele-de-France'), ('Ouest de la France', 'Ouest de la France'), ('Nord de la France', 'Nord de la France'), ('Est de la France', 'Est de la France'), ('Sud de la France', 'Sud de la France'), ('Toute la France', 'Toute la France'), ('\xc9tranger', '\xc9tranger')]),
        ),
    ]
