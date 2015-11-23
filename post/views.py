#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from post.forms import AnnonceForm
from post.models import Annonce

class AnnonceCreate(CreateView):
    """ Partie qui gère le formulaire de mise en ligne auto d'annonce """
    model = Annonce
    template_name = 'post/formulaire.html'
    form_class = AnnonceForm
    success_url = '/post/success'

    @method_decorator(login_required)
    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(AnnonceCreate, self).dispatch(*args, **kwargs)

class SuccessView(TemplateView):
    """ Vue affichée une fois la mise en ligne auto effectuée """
    template_name = 'post/success.html'

    def get_context_data(self, **kwargs):
        # Récupération du contexte existant
        context = super(SuccessView, self).get_context_data(**kwargs)

        # Ajout du contexte nécessaire à post/success.html
        context['annonce'] = Annonce.objects.order_by('-pub_date')[0]
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SuccessView, self).dispatch(*args, **kwargs)
