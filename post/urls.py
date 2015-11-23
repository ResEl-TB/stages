#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import AnnonceCreate, SuccessView

urlpatterns = [
	url(r'^$', AnnonceCreate.as_view(), name='auto'), # Vue accueil de la partie post, avec le formulaire de dépot automatique
	url(r'^success$', SuccessView.as_view(), name='success'), # Modo automatique effectuée, annonce en ligne
]
