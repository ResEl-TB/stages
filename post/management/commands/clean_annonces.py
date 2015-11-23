#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.core.mail import send_mail

from post.models import Annonce

class Command(BaseCommand):
    help = 'Supprime une annonce si sa durée de vie est dépassée.'

    def handle(self, *args, **options):
        annonces = Annonce.objects.all()

        for annonce in annonces:
            if annonce.pub_date < timezone.now() - timedelta(days=180):
                annonce.delete()
