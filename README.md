# Stages
Plate-forme de stages pour Télécom Bretagne

## Description
  Cette plate-forme a été développée pour le service stages de l'école Télécom Bretagne.
  L'idée est simple : le service peut déposer en ligne une annonce de stage ou d'alternance via une URL ou un fichier PDF.
  Afin de permettre une recherche de la part des étudiants, le dit service doit renseigner des champs tels
  que la durée du contrat, le domaine concerné, etc.
  
  Du côté des étudiants, ils peuvent effectuer une recherche selon leurs propres critères, et parcourir les
  annonces comme ils le souhaitent. Dès qu'une annonce est pourvue, c'est à l'étudiant de faire le nécessaire
  pour avertir le département stages que la dite annonce n'est plus disponible.
  
  Un système de crontab fait que dès qu'une annonce est vieille de plus de 6 mois à compter de la date de publication,
  elle est supprimée.
  
## Accès
  Le site est accessible à l'adresse https://stages.resel.fr
  
  Seules les personnes possédant un compte au sein de l'école sont autorisées à parcourir le site,
  ceci afin d'éviter que des offres de stages réservées aux étudiants de Télécom Bretagne ne soient
  accessible à la vue de tous.
