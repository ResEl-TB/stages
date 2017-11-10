# Le site stages.resel.fr

Ce dépôt contient le code source du site [stages.resel.fr](https://stages.resel.fr)
Ce site est développé en [Python](https://python.org/) avec le framework [Django](https://www.djangoproject.com/).
Ce document a pour but de présenter les différents modules de ce site.

## Description

Cette plate-forme a été développée pour le service stages de l'école Télécom Bretagne.
L'idée est simple : le service peut déposer en ligne une annonce de stage ou d'alternance via une URL ou un fichier PDF.
Afin de permettre une recherche de la part des étudiants, le dit service doit renseigner des champs tels
que la durée du contrat, le domaine concerné, etc.

Du côté des étudiants, ils peuvent effectuer une recherche selon leurs propres critères, et parcourir les
annonces comme ils le souhaitent. Dès qu'une annonce est pourvue, c'est à l'étudiant de faire le nécessaire
pour avertir le département stages que la dite annonce n'est plus disponible.

Un cron tourne chaque jour pour lancer la commande `python3 manage.py clean_announces` qui se charge de supprimer les annonces vieilles de plus de 3 mois.

Un middleware se charge de donner l'accès admin au site aux admins ResEl lors de leur connexion.

## Accès
Le site est accessible à l'adresse https://stages.resel.fr

Seules les personnes possédant un compte au sein de l'école sont autorisées à parcourir le site,
ceci afin d'éviter que des offres de stages réservées aux étudiants de Télécom Bretagne ne soient
accessible à la vue de tous.

# Démarrage rapide

```
git clone https://git.resel.fr/resel/stages.git stages
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
cp stages/settings_local.tpl stages/settings_local.py
```

Éditez ensuite le fichier `stages/settings_local.py` pour renseigner le chemin absolu de votre base de donnée sqlite (en général `project_path/db.sqlite3`)

Effectuez les premières migrations (`python manage.py migrate`), créez vous un superuser (`python manage.py createsuperuser`) et enfin lancez le serveur (`python manage.py runserver`).

Accédez enfin au site `http://localhost:8000/login_local` avec votre superuser.

# Les modules

## `pages`

Contient différentes petites choses nécessaires au site.

- Les templatetags
  - `add_css` : permet d'ajouter une classe css au field Django
  - `url_replace` : permet de conserver les résultats de la recherche au changement de page (le pager de Django est pas au point là-dessus)
- Les context processors
  - `mobile` : identifie si le device qui accède au site est un mobile ou pas. Cela permet dans le détail de l'annonce de proposer au utilisateurs sur téléphone de télécharger les annonces pdf au lieu de les afficher dans la page.

## `post`

Module qui permet de créer une annonce.

Contient les modèles de l'objet `Annonce` ainsi qu'un petit formulaire de dépôt et les vues/templates associés.

## `search`

Module qui permet de chercher une annonce.

Contient la logique de filtrage dans la requête GET pour trier les annonces.

# Les subtilités

Le script `clear_sessions.sh` permet de nettoyer la base de donner en virant les sessions expirées de Django. Il s'agit d'une bonne pratique recommandée par Django.