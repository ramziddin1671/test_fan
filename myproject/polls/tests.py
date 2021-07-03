from django.test import TestCase
from django.urls import reverse
from .models import Category, Question, Choice


# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Biologiya')

    def test_text_content(self):
          category = Category.objects.get(id=1)
          expected_object_name = f'{category.name}'
          self.assertEqual(expected_object_name, "Biologiya")

class HomePageViewTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Biologiya2')

    def test_views_url_exists_at_proper_location(self):

      resp = self.client.get('/')
      self.assertEqual(resp.status_code, 200)




