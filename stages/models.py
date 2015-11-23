#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Contact(models.Model):
	""" Modèle servant au contact des modo """

	message = models.TextField(
			verbose_name = "Décrivez votre demande ici",
		)

	contact = models.EmailField(
			verbose_name = "Contact",
		)
