#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone

from .models import RechercheFields
from post.models import Domaine

class RechercheForm(forms.ModelForm):
    """ Formulaire pour rechercher parmi les annonces existantes """

    class Meta:
	model = RechercheFields
	fields = [
		'zone', 'nom_entreprise', 'domain', 'duree', 'type_de_contrat',
	]
	widgets = {
                'domain': forms.SelectMultiple(attrs={'size': str(Domaine.objects.count())}),
        }
  
    def clean_nom_entreprise(self):
    	return self.cleaned_data['nom_entreprise'].encode('utf8')
