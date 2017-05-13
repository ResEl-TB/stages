from django.contrib import admin
from .models import Annonce, Domaine, Zone, TypeContrat, Organisme, Duree
from django.contrib.auth.models import Group

# Classe qui sert à mettre en forme la gestion des annonces
class AnnonceAdmin(admin.ModelAdmin):
    fieldsets = [
	   ('Informations indispensables', {
            'fields': ['zone', 'nom_entreprise', 'type_de_contrat', 'duree', 'domain']
        }),
	   ("Accès à l'annonce - Renseignez au moins un champ", {
            'fields': ['url', 'file', 'multiple_files']
        }),
	   ('Informations optionnelles', {
            'fields': ['ville', 'date_debut', 'type_organisme', 'commentaires']
        }),
    ]
    list_display = ('id', 'nom_entreprise', 'zone', 'type_de_contrat', 'domaines', 'pub_date', 'visites') 
    list_filter = ['pub_date', 'type_de_contrat', 'zone', 'domain']
    search_fields = ['nom_entreprise', 'id']

    def domaines(self, obj):
        return ", ".join([d.nom for d in obj.domain.all()])

admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Domaine)
admin.site.register(Zone)
admin.site.register(TypeContrat)
admin.site.register(Organisme)
admin.site.register(Duree)
admin.site.unregister(Group)