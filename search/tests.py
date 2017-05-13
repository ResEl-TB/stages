from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from post.models import Zone, Duree, Domaine, TypeContrat, Annonce
from .forms import SearchForm

class SearchForms(TestCase):
    def setUp(self):
        zone = Zone.objects.create(nom='île-de-france')
        duree = Duree.objects.create(duree='6 mois')
        domain = Domaine.objects.create(nom='Télécoms')
        contract = TypeContrat.objects.create(type_contrat='stage')
        for i in range(5):
            Annonce.objects.create(
                zone=zone,
                duree=duree,
                type_de_contrat=contract
            ).domain.add(domain)

    def test_search_empty(self):
        form = SearchForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.build_queryset()), 5)

    def test_search_not_empty(self):
        form = SearchForm(data={'nom_entreprise': 'thales'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.build_queryset()), 0)

    def test_search_zone(self):
        form = SearchForm(data={'zone': 1})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.build_queryset()), 5)

    def test_search_domain(self):
        form = SearchForm(data={'domain': [1]})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.build_queryset()), 5)

class SearchViews(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'john@smith.com', 'password')
        zone = Zone.objects.create(nom='île-de-france')
        duree = Duree.objects.create(duree='6 mois')
        domain = Domaine.objects.create(nom='Télécoms')
        contract = TypeContrat.objects.create(type_contrat='stage')
        for i in range(5):
            Annonce.objects.create(
                zone=zone,
                duree=duree,
                type_de_contrat=contract
            ).domain.add(domain)

    def test_index_login(self):
        response = self.client.get(reverse('search:index'))
        self.assertEqual(response.status_code, 302)

    def test_index_normal(self):
        self.client.login(username='john', password='password')
        response = self.client.get(reverse('search:index'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/index.html')
        self.assertEqual(len(response.context.get('object_list')), 5)

    def test_index_search(self):
        self.client.login(username='john', password='password')
        response = self.client.get(reverse('search:index'), {'zone': '1'})
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/index.html')
        self.assertEqual(len(response.context.get('object_list')), 5)