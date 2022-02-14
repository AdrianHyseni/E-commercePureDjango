from unittest import skip
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Category, Product
from store.views import product_all

# @skip("demostrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

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
        response = product_alls(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>')
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('item/django-bbb')
        response = product_alls(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code,200)

    def test_url_allowed_hosts(self):
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)
            

    

    



