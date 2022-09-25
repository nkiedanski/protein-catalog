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

    def test_get_proteins(self):
        kinase1 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase1]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(my_catalog.get_proteins(), my_list_kinases)

    def test_set_proteins(self):
        kinase1 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase1]
        my_catalog = Catalog(my_list_kinases)
        kinase1.set_organism("bacteria")
        my_list_kinases = [kinase1]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(my_catalog.get_proteins(), my_list_kinases)

    def test_max_spacing_for_all_proteins(self):
        kinase1 = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase1, kinase2]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(my_catalog.max_spacing_for_all_proteins(), 25)

    def test_max_spacing_headers_invalid(self):
        kinase1 = Protein("3C", "tran", "Homo", "200", True, "3")
        kinase2 = Protein("4LT", "tran", "Alkal", "201", True, "2")
        headers = ["-", "-", "-", "-"]
        my_list_kinases = [kinase1, kinase2]
        my_catalog = Catalog(my_list_kinases)
        self.assertNotEqual(13, my_catalog.max_spacing_headers())

    def test_generate_headers(self):
        kinase1 = Protein("3C", "tran", "Homo", "200", True, "3")
        my_list_kinases = [kinase1]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(my_catalog.generate_headers(), "--PDBcode--           --Classification--    --Organism--          "
                                                        "--YearDeposited--     --ManuallyCrurated--  --AtomCount--         ")

    def test__str__(self):
        kinase1 = Protein("3C", "tran", "Homo", "200", True, "3")
        my_list_kinases = [kinase1]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(
            my_catalog.__str__(),
             "--PDBcode--           --Classification--    --Organism--          "
             "--YearDeposited--     --ManuallyCrurated--  --AtomCount--         \n"
             "3C                    tran                  Homo                  "
             "200                   True                  3                     \n"
        )

