from dataclasses import is_dataclass
from category.domain.entities import Category
import unittest

class TestCategoryUnit(unittest.TestCase):

    def test_if_is_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(name='Nome Sobrenome', 
                            email='nome.sobrenome@gmail.com', 
                            phone='99999999999')
        self.assertEqual(category.name, 'Nome Sobrenome') # O que eu quero testar (category.name) || Valor esperado 'Nome Sobrenome'
        self.assertEqual(category.email, 'nome.sobrenome@gmail.com')
        self.assertEqual(category.phone, '99999999999')