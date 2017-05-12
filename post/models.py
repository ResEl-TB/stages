from django.utils import timezone
from django.db import models

from .validators import validate_file_extension

class Zone(models.Model):
    class Meta:
        verbose_name = 'zone géographique'
        verbose_name_plural = 'zones géographique'
        
    nom = models.CharField(
        verbose_name='Zone géographique du stage',
        max_length=50,
    )

    def __str__(self):
        return self.nom

class Duree(models.Model):
    class Meta:
        verbose_name = 'durée'

    duree = models.CharField(
        verbose_name='Durée du contrat',
        max_length=50,
    )

    def __str__(self):
        return self.duree

class Domaine(models.Model):
    nom = models.CharField(
        verbose_name='Nom du domaine',
        max_length=200,
    )

    def __str__(self):
        return self.nom 

class Organisme(models.Model):
    type_organisme = models.CharField(
        verbose_name='Type d\'organisme',
        max_length=100,
        null=True,
    )

    def __str__(self):
        return self.type_organisme

class TypeContrat(models.Model):
    class Meta:
        verbose_name = 'type de contrat'
        verbose_name_plural = 'types de contrat'

    type_contrat = models.CharField(
        verbose_name='Nature du contrat',
        max_length=100,
    )

    def __str__(self):
        return self.type_contrat

class Annonce(models.Model):
    """ Modèle pour mettre en ligne sans modération manuelle une annonce """

    # Définition des différents champs
    zone = models.ForeignKey(
        'Zone',
        blank=False,
        verbose_name='Localisation de l\'annonce',
    )

    ville = models.CharField(
        verbose_name="Ville",
        max_length=30,
        blank=True,
    )

    date_debut = models.CharField(
        verbose_name='Date de début du contrat',
        max_length=10,
        default='',
        blank=True,
    )  

    duree = models.ForeignKey(
        'Duree',
        verbose_name='Durée du contrat',
        blank=False,
    )

    domain = models.ManyToManyField(
        'Domaine', 
        blank=False, 
        verbose_name='Domaine concerné',
        help_text='Maintenir la touche Ctrl pour choisir plusieurs domaines',
    )

    type_organisme = models.ForeignKey(
        'Organisme',
        verbose_name='Type d\'organisme',
        blank=True,
        null=True
    )

    nom_entreprise = models.CharField(
        verbose_name='Nom de l\'entreprise',
        max_length=40,
        blank=False,
    )

    type_de_contrat = models.ForeignKey(
        'TypeContrat',
        verbose_name='Type de contrat',
        default=1,
        blank=False,
    )

    fichier = models.FileField(
        verbose_name='Fichier contenant l\'annonce',
        blank=True,
        default='',
        upload_to='annonces/%Y/%m/%d',
        validators=[validate_file_extension],
    )

    multiple_files = models.BooleanField(
        verbose_name='Le fichier contient plusieurs annonces ?',
        blank=False,
        default=False,
    )

    url_annonce = models.URLField(
        verbose_name='URL vers l\'annonce',
        default='',
        blank=True,
    )

    commentaires = models.TextField(
        verbose_name='Commentaires à propos de l\'annonce',
        blank=True,
    )

    pub_date = models.DateTimeField(
        verbose_name='Date de publication',
        auto_now=False,
        auto_now_add=True,
        editable=False
    )

    visites = models.IntegerField(
        verbose_name='Visites',
        editable=False,
        default=0,
    )

    def __str__(self):
        return '%s - %s - %s - %s' % (self.nom_entreprise, self.zone, self.type_de_contrat, self.domain)

    # Méthode permettant d'itérer sur les champs du modèle
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
