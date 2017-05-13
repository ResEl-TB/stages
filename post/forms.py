from django import forms
from django.utils import timezone
from django.utils.safestring import mark_safe

from post.models import Annonce, Domaine, Zone

import re

class AnnonceForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        label=u'zone géographique',
        queryset=Zone.objects.exclude(nom__contains='toute'),
        empty_label='',
        required=True
    )
    multiple_files = forms.BooleanField(
        required=False
    )

    class Meta:
        model = Annonce
        fields = '__all__'
        widgets = {
            'domain': forms.SelectMultiple(attrs={'size': str(Domaine.objects.count())}),
            'ville': forms.TextInput(attrs={'placeholder': 'Ville où se déroule le contrat'}),
            'commentaires': forms.Textarea(attrs={'rows': '5'}),
        }