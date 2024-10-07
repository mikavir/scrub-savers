import os
if os.path.exists("env.py"):
    import env  # noqa
from django.test import TestCase
from django.test import Client
from .models import Product
from django.contrib.auth.models import User

# Creating superuser to test admin views:
# https://stackoverflow.com/questions/3495114/how-to-create-admin-user-in-django-tests-py
password = os.environ.get("TEST_PASSWORD")
email = os.environ.get("TEST_EMAIL")


# Create your tests here.
class TestViews(TestCase):

    def test_all_product_page(self):
        """ Testing views for all product page """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_page(self):
        """ Test views for product detail page"""
        # Create product
        product = Product.objects.create(
            name='Test2', price=30, description="test"
            )
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product(self):
        """ Test views for add product: limited to admin users"""
        # https://stackoverflow.com/questions/33274874/assertionerror-302-200
        # Log superuserin
        self.client = Client()
        user = User.objects.create_superuser('test_admin', password)
        self.client.force_login(user=user)
        # Test if url resposnse is correct
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_delete_product(self):
        """ Test views for delete product: limited to admin users"""
        # Create test product
        product = Product.objects.create(
            name='Test4', price=30, description="test"
            )
        # Log admin
        self.client = Client()
        user = User.objects.create_superuser('test_admin', password)
        self.client.force_login(user=user)
        # Delete Product to test url
        self.client.get(f'/products/delete/{product.id}/')
        # Check if product exists
        existing_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(existing_product), 0)
