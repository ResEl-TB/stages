#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ContactForm
from .models import Contact

class ContactView(View):
	model = Contact
	form_class = ContactForm
	template_name = 'stages/contact.html'
	mail_sent = False

	@method_decorator(login_required(login_url = '/login'))
    	def dispatch(self, *args, **kwargs):
        	return super(ContactView, self).dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
		self.form = self.form_class()
		return render(request, self.template_name, {'form': self.form, 'mail_sent': self.mail_sent})

	def post(self, request, *args, **kwargs):
		self.form = self.form_class(self.request.POST or None)

		if self.form.is_valid():
			message = self.form.cleaned_data['message']
			contact = self.form.cleaned_data['contact']
			contenu_mail = message
			mail = EmailMessage(
				subject = "[Stages] Un utilisateur requiert votre attention",
				body = contenu_mail,
				from_email = contact,
				reply_to = [contact],
				to = [ "stages-admin@resel.fr" ],
			)
			mail.send()
			self.mail_sent = True

		return render(request, self.template_name, {'form': self.form, 'mail_sent': self.mail_sent})
