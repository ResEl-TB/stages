#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

# Sert à restreindre l'upload des fichiers
def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext in valid_extensions:
        raise forms.ValidationError(u'Fichier non pris en charge, veuillez uploader un fichier au format pdf')
