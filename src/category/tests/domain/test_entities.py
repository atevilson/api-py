from category.domain.entities import Category
import unittest

class TestCategory(unittest.TestCase):
    def test_constructor(self):
        category = Category('Nome Sobrenome', 'nome.sobrenome@gmail.com', '99999999999')
        self.assertEqual(category.name, 'Nome Sobrenome')
        self.assertEqual(category.email, 'nome.sobrenome@gmail.com')
        self.assertEqual(category.phone, '99999999999')