import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_pagina_inicial(self):
        response = self.client.get('/')
        self.assertContains(response, 'Pagina Inicial', 1, 200)

    def test_contato(self):
        response = self.client.get('/contato')
        self.assertContains(response, 'Contato', 3, 200)

    def test_desenvolvido(self):
        response = self.client.get('/desenvolvido')
        self.assertContains(response, 'Desenvolvido', 3, 200)
