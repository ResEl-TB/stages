#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	""" Formulaire de contact des admins """

	class Meta:
		model = Contact
		fields = [
			'contact', 'message',
		]
		widgets = {
			'message': forms.Textarea,
		}

	# Pour résoudre les soucis d'encodage unicode
	def clean_message(self):
		return self.cleaned_data['message'].encode('utf8')
