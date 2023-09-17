from django.test import TestCase, RequestFactory
from django.urls import reverse
from seller.views import register

class RegisterTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_register_method(self):
        request = self.factory.get(reverse('register'))

        response = register(request)

        self.assertEqual(response.status_code, 200)
