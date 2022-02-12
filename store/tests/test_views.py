from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django bGuide', created_by_id=1, slug='djanog-bbb', price='20.00', image='images/')


    def test_url_allowed_host(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['djanog-bbb']))
        self.assertEqual(response.status_code,200)
    
    def test_category_detail_url(self):
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code,200)


#test by HTTP REQUESTS
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>',html)
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('item/django-bbb')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>',html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code,200)


    



