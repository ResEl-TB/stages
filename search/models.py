#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models

import post.models

class RechercheFields(models.Model):
    """ Modèle pour rechercher des annonces """

    # Définition des différents champs
    zone = models.ForeignKey(
		post.models.Zone,
		verbose_name = "Zone géographique",
		blank = True,
		null = True,
	)

    domain = models.ManyToManyField(
		post.models.Domaine,
		verbose_name = "Domaine concerné",
		blank = True,
	)

    duree = models.ForeignKey(
		post.models.Duree,
		verbose_name = "Durée du contrat",
		blank = True,
		null = True,
	)

    type_de_contrat = models.ForeignKey(
		post.models.TypeContrat,
		verbose_name = "Nature du contrat",
		blank = True,	
		null = True,
	)

    nom_entreprise = models.CharField(
                verbose_name = "Nom de l'entreprise",
                max_length = 40,
                blank = True,
        )
