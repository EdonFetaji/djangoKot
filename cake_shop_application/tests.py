from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Baker, Cake
from .forms import CakeForm


class BakerModelTest(TestCase):
    def test_str(self):
        baker = Baker(name="Alice", surname="Smith", phone_number="123")
        self.assertEqual(str(baker), "Alice Smith | 123")


class CakeModelTest(TestCase):
    def test_str(self):
        cake = Cake(name="Chocolate Cake")
        self.assertEqual(str(cake), "Chocolate Cake")


class CakeFormTest(TestCase):
    def test_valid_form(self):
        form = CakeForm(data={
            'name': 'Vanilla Cake',
            'price': 15.5,
            'weight': 1.0,
            'description': 'Tasty',
        })
        self.assertTrue(form.is_valid())



class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.baker = Baker.objects.create(user=self.user, name="John", surname="Doe")

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_cake_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('add_cake'), {
            'name': 'Strawberry Cake',
            'price': 10.0,
            'weight': 0.5,
            'description': 'Fresh',
        })
        self.assertEqual(response.status_code, 302)  # should redirect
        self.assertEqual(Cake.objects.count(), 1)
        self.assertEqual(Cake.objects.first().baker, self.baker)
