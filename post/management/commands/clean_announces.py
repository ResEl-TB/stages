#!/usr/bin/env python

from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.core.files import File

from post.models import Annonce

class Command(BaseCommand):
    help = 'clean the old announces (older than 3 months)'

    def handle(self, *args, **options):
        annonces = Annonce.objects.all()

        for annonce in annonces:
            if annonce.pub_date < timezone.now() - timedelta(days=180):
                try:
                    annonce.delete()
                except:
                    open('/tmp/dummy', 'a').close()
                    annonce.fichier = File(open('/tmp/dummy', 'r'))
                    annonce.save()
                    annonce.delete()
