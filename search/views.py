#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView
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
    form = form_class()
    nb_annonces = Annonce.objects.all().count()
    paginate_by = 20
    queryset = Annonce.objects.all().order_by('-pub_date')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(**kwargs)
        context['form'] = self.form
	context['nb_annonces'] = self.nb_annonces
        context['range_pages'] = range(1, int(self.nb_annonces / self.paginate_by) + 2)
	return context

    def get(self, request, *args, **kwargs):
        self.form = self.form_class(self.request.GET)
	page = request.GET.get('page', '')
	if page == '' and 'champs' in request.session:
            del request.session['champs']
	#if 'champs' in request.session:
	#    if self.nb_annonces != Annonce.objects.all().count():
	#    	del request.session['champs']
	return super(IndexView, self).get(request, *args, **kwargs)

    def get_queryset(self):
	annonces = Annonce.objects.all().order_by('-pub_date')
	if 'champs' in self.request.session:
	    champs = self.request.session['champs']
	    for key, value in champs.items():
	        if value != None:
		    if key == 'zone':
		        annonces = annonces.filter(zone__id = value.id)
		    elif key == 'nom_entreprise':
			if value != '':
			    annonces = annonces.filter(nom_entreprise__icontains = value)
		    elif key == 'duree':
			annonces = annonces.filter(duree__id = value.id)
		    elif key == 'type_de_contrat':
			annonces = annonces.filter(type_de_contrat__id = value.id)
		    elif key == 'domain':
			for domaine in value:
			    annonces = annonces.filter(domain__id = domaine.id)
	self.nb_annonces = annonces.count()
	return annonces

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(self.request.POST)
        if self.form.is_valid():
	    request.session['champs'] = self.form.cleaned_data
        return super(IndexView, self).get(request, *args, **kwargs)

class DetailView(DetailView):
    model = Annonce
    template_name = 'search/annonce.html'

    def get_object(self):
        # Call the superclass
        object = super(DetailView, self).get_object()
        # Record the last accessed date
        object.visites += 1
        object.save()
        # Return the object
        return object

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

