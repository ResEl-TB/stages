from django import forms

from post.models import Domaine, Zone, Duree, TypeContrat, Annonce

class SearchForm(forms.Form):
    zone = forms.ModelChoiceField(queryset=Zone.objects.all(), empty_label=None, required=False)
    nom_entreprise = forms.CharField(max_length=40, required=False)
    domain = forms.ModelMultipleChoiceField(queryset=Domaine.objects.all(), required=False)
    duree = forms.ModelChoiceField(queryset=Duree.objects.all(), empty_label=None, required=False)
    type_de_contrat = forms.ModelChoiceField(queryset=TypeContrat.objects.all(), empty_label=None, required=False)

    def build_queryset(self):
        data = self.cleaned_data
        d = {}
        for key, value in data.items():
            if value:
                if key == 'nom_entreprise':
                    d[key+'__contains'] = value
                elif key == 'domain':
                    d[key+'__pk__in'] = [_.pk for _ in value]
                else:
                    d[key+'__pk'] = value.pk
        return Annonce.objects.filter(**d) if len(d) != 0 else Annonce.objects.all()