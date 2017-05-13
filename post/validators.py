from django import forms
import os

# Sert à restreindre l'upload des fichiers
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext in valid_extensions:
        raise forms.ValidationError('Fichier non pris en charge, veuillez uploader un fichier au format pdf')
