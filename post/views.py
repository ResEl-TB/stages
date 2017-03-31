#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

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

    def get_success_url(self):
	self.request.session['annonce'] = self.object
	return reverse('post:success')

class SuccessView(TemplateView):
    """ Vue affichée une fois la mise en ligne auto effectuée """
    template_name = 'post/success.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SuccessView, self).dispatch(*args, **kwargs)
