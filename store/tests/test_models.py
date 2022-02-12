from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1  = Category.objects.create(name='django', slug='django')

        def test_category_model_entry(self):

            data = self.data1
            self.assertTrue(isinstance(data, Category))


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django bGuide', created_by_id=1, slug='djanog-bbb', price='20.00', image='images/')

    def test_product_model(self):
        data = self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data), 'django bGuide')


    