from django import forms
from django.utils import timezone
from django.utils.safestring import mark_safe

from post.models import Annonce, Domaine

import re

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe('\n'.join(['%s\n' % w for w in self]))

class AnnonceForm(forms.ModelForm):
    """ Formulaire pour poster directement sans intervention manuelle une annonce """

    class Meta:
        model = Annonce
        fields = '__all__'
        widgets = {
            'domain': forms.SelectMultiple(attrs={'size': str(Domaine.objects.count())}),
            'ville': forms.TextInput(attrs={'placeholder': 'Ville où se déroule le contrat'}),
            'date': forms.TextInput(attrs={'placeholder': 'Début du stage'}),
            'commentaires': forms.Textarea(attrs={'rows': '5'}),
            'multiple_files': forms.RadioSelect(renderer = HorizontalRadioRenderer),
        }