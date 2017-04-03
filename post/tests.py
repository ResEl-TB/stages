from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .forms import AnnonceForm
from .models import Zone, Duree, Domaine, TypeContrat

class PostForms(TestCase):
    def setUp(self):
        Zone.objects.create(nom='île-de-france')
        Duree.objects.create(duree='6 mois')
        Domaine.objects.create(nom='Télécoms')
        TypeContrat.objects.create(type_contrat='stage')

    def test_annonce(self):
        form = AnnonceForm(data={
            'zone': 1,
            'duree': 1,
            'domain': [1],
            'nom_entreprise': 'orange',
            'type_de_contrat': 1,
            'multiple_files': 0,
        })
        self.assertTrue(form.is_valid())

class PostViews(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'john@smith.com', 'password', is_staff=True)
        Zone.objects.create(nom='île-de-france')
        Duree.objects.create(duree='6 mois')
        Domaine.objects.create(nom='Télécoms')
        TypeContrat.objects.create(type_contrat='stage')

    def test_create_annonce_login(self):
        response = self.client.get(reverse('post:creation'))
        self.assertEquals(response.status_code, 302)
        self.client.login(username='john', password='password')
        response = self.client.get(reverse('post:creation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/creation.html')

    def test_create_annonce_normal(self):
        self.client.login(username='john', password='password')
        response = self.client.post(
            reverse('post:creation'), 
            {
                'zone': 1,
                'duree': 1,
                'domain': [1],
                'nom_entreprise': 'orange',
                'type_de_contrat': 1,
                'multiple_files': 0,
            }
        )
        self.assertEqual(response.status_code, 302)