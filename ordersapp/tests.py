from django.test import TestCase
from django.test.client import Client
from ordersapp.models import Order
from django.core.management import call_command


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()
        self.checked_order = Order.objects.get(pk=3)

    def test_get_total_quantity(self):
        self.assertEqual(self.checked_order.get_total_quantity(), 3)

    def get_product_type_quantity(self):
        self.assertEqual(self.checked_order.get_product_type_quantity(), 2)

    def test_get_total_cost(self):
        self.assertEqual(self.checked_order.get_total_cost(), 9670.00)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')
