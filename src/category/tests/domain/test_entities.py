from category.domain.entities import Category
import unittest

class TestCategory(unittest.TestCase):
    def test_constructor(self):
        category = Category('Atevilson Freitas', 'freitas.atevilson@gmail.com', '44999999999')
        self.assertEqual(category.name, 'Atevilson Freitas')
        self.assertEqual(category.email, 'freitas.atevilson@gmail.com')
        self.assertEqual(category.phone, '44999999999')