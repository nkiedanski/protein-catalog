import unittest
from ..protein import Protein
from ..catalog import Catalog


class TestCatalog(unittest.TestCase):

    def test_initialize_catalog_with_valid_proteins(self):
        kinase1 = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase1, kinase2]
        my_catalog = Catalog(my_list_kinases)
        self.assertTrue(isinstance(my_catalog, Catalog))

    def test_initialize_catalog_with_invalid_list_of_proteins(self):
        kinase1 = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinase2 = "4LTR"
        my_list_kinases = [kinase1, kinase2]
        try:
            Catalog(my_list_kinases)
            catalog_created = True
        except TypeError:
            catalog_created = False
        self.assertFalse(catalog_created)