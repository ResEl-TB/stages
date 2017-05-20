from django import forms

from post.models import Domaine, Zone, Duree, TypeContrat, Annonce

class SearchForm(forms.Form):
    zone = forms.ModelChoiceField(
        label=u'zone géographique',
        queryset=Zone.objects.all(),
        empty_label='',
        required=False
    )
    nom_entreprise = forms.CharField(
        label=u'nom de l\'entreprise',
        max_length=40,
        required=False
    )
    domain = forms.ModelMultipleChoiceField(
        label=u'domaine de l\'emploi',
        queryset=Domaine.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': Domaine.objects.count()})
    )
    duree = forms.ModelMultipleChoiceField(
        label=u'durée',
        queryset=Duree.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': Duree.objects.count()})
    )
    type_de_contrat = forms.ModelChoiceField(
        label=u'type du contrat',
        queryset=TypeContrat.objects.all(),
        empty_label='',
        required=False
    )

    def build_queryset(self):
        self.is_valid()
        data = self.cleaned_data
        d = {}
        for key, value in data.items():
            if value:
                if key == 'nom_entreprise':
                    d[key+'__contains'] = value
                elif key == 'domain':
                    d[key+'__pk__in'] = [_.pk for _ in value]
                elif key == 'zone':
                    if 'toute' not in value.nom.lower():
                        d[key+'__pk'] = value.pk
                else:
                    d[key+'__pk'] = value.pk
        results = Annonce.objects.filter(**d) if len(d) != 0 else Annonce.objects.all()
        return results.order_by('-pub_date')