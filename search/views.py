#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from post.models import Annonce
from search.forms import RechercheForm

class IndexView(ListView):
    model = Annonce
    form_class = RechercheForm
    template_name = 'search/index.html'
    context_object_name = 'annonces'
    queryset = Annonce.objects.all()
    form = form_class()
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(**kwargs)
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        self.form = self.form_class(self.request.GET or None)
	if 'champs' in request.session:
	    del request.session['champs']
	return super(IndexView, self).get(request, *args, **kwargs)

    def get_queryset(self):
	annonces = Annonce.objects.all()
	if 'champs' in self.request.session:
	    champs = self.request.session['champs']
	    temp = list()
	    for key, value in champs.items():
	        if value != None:
		    if key == 'zone':
		        temp += annonces.filter(zone__nom = value.nom)
		    elif key == 'nom_entreprise':
			temp += annonces.filter(nom_entreprise = value)
		    elif key == 'duree':
			temp += annonces.filter(duree__duree = value.duree)
		    elif key == 'type_de_contrat':
			temp += annonces.filter(type_de_contrat__type_contrat = value.type_contrat)
		    elif key == 'domain':
			for domaine in value:
			    temp += annonces.filter(domain__nom = domaine.nom)
	    annonces = list()
	    for annonce in temp:
		if annonce not in annonces:
		    annonces.append(annonce)	
	return annonces

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(self.request.POST or None)
        if self.form.is_valid():
	    request.session['champs'] = self.form.cleaned_data
        return super(IndexView, self).get(request, *args, **kwargs)

class DetailView(DetailView):
    model = Annonce
    template_name = 'search/annonce.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)
