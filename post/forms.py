#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone

from post.models import Annonce, Domaine

import re

from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class AnnonceForm(forms.ModelForm):
	""" Formulaire pour poster directement sans intervention manuelle une annonce """

	class Meta:
		model = Annonce
		fields = [
			# Les champs obligatoires :
			'zone', 'nom_entreprise', 'type_de_contrat', 'duree', 'domain', 
			# Les champs pour accéder à l'annonce
			'url_annonce', 'fichier', 'multiple_files',
			# Les champs optionnels :
			'ville', 'date_debut', 'type_organisme', 'commentaires'
		]
		widgets = {
			'domain': forms.SelectMultiple(attrs={'size': str(Domaine.objects.count())}),
			'ville': forms.TextInput(attrs={'placeholder': 'Ville où se déroule le contrat'}),
			'date': forms.TextInput(attrs={'placeholder': 'Début du stage'}),
			'commentaires': forms.Textarea(attrs={'rows': '5'}),
			'multiple_files': forms.RadioSelect(renderer = HorizontalRadioRenderer),
		}

	# Contrôle de la validité de la date de début de stage
	def clean_date_debut(self):
		date = self.cleaned_data['date_debut']
		if date == '':
		    return date
		if not re.search(r'^[0-3][0-9]/[0-1][0-9]/20[1-2][0-9]$', date):
			raise forms.ValidationError("Choisissez la date sur le calendrier.")
		now = timezone.localtime(timezone.now())
		day = int(date.split('/')[0])
		month = int(date.split('/')[1])
		year = int(date.split('/')[2])
		if (year < now.year) or (year == now.year and month < now.month) or (year == now.year and month == now.month and day < now.day):
			raise forms.ValidationError("Vous avez vraiment entré une date passée ? ...")
		return date

	def clean_ville(self):
		return self.cleaned_data['ville'].encode('utf8').lower()

	def clean_nom_entreprise(self):		
		return self.cleaned_data['nom_entreprise'].encode('utf8')

	def clean_commentaires(self):
		return self.cleaned_data['commentaires'].encode('utf8')
