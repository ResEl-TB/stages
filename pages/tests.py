from django.test import TestCase
from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from pages.forms import ContactForm

class PagesForms(TestCase):
    def test_contact(self):
        self.assertFalse(
            ContactForm(data={
                'email': 'machintruc.fr',
                'message': 'Bonjour, je suis un test de mail'
            }).is_valid()
        )

        form = ContactForm(data={
            'email': 'machin@truc.fr',
            'message': 'Bonjour, je suis un test de mail'
        })
        self.assertTrue(form.is_valid())
        form.send_email()
        self.assertEqual(len(mail.outbox), 1)

class PagesViews(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'john@smith.com', 'password')

    def test_contact_login(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 302)
        self.client.login(username='john', password='password')
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_contact_full(self):
        self.client.login(username='john', password='password')
        response = self.client.post(reverse('contact'), {'email': 'machin@truc.fr', 'message': 'testing'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)