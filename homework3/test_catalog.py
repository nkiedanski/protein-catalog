import unittest
import pandas as pd

from database import Database
from protein import Protein
from catalog import Catalog

class TestCatalog(unittest.TestCase):

    def test_add_protein_no_addition(self):
        my_catalog = Catalog()
        result = my_catalog.add_protein_if_not_exist("3C49","transferasa","Homo sapiens","2008-01-29",True,"357")
        self.assertEqual(result, False)

    def test_add_protein_addition(self):
        my_catalog = Catalog()
        result = my_catalog.add_protein_if_not_exist("NICOLE", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(result, True)


if __name__ == '__main__':
        unittest.main()