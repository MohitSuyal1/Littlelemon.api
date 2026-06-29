from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(name="Pasta", price=250, description="Creamy Alfredo pasta")
        self.assertEqual(item.name, "Pasta")
        self.assertEqual(str(item), "Pasta")
