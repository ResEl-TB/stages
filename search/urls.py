#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import IndexView, DetailView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'), # Vue accueil de la partie recherche
	url(r'^announce/(?P<pk>[0-9]+)$', DetailView.as_view(), name='detail'),  # Vue d'une annonce
]