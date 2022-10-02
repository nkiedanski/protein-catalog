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

    def test_read_catalog(self):
        my_catalog = Catalog.read_catalog("/Users/nicole/PycharmProjects/python-ii/test_read_catalog.txt")
        self.assertEqual(len(my_catalog.get_proteins()), 2)
        self.assertEqual(my_catalog.get_proteins()[0].get_pdb_code(), "3C49")
        self.assertEqual(my_catalog.get_proteins()[0].get_classification(), "transferasa")
        self.assertEqual(my_catalog.get_proteins()[0].get_organism(), "Homo sapiens")
        self.assertEqual(my_catalog.get_proteins()[1].get_year_deposited(), "2013-07-23")
        self.assertEqual(my_catalog.get_proteins()[1].get_manually_curated(), True)
        self.assertEqual(my_catalog.get_proteins()[1].get_atom_count(), "152")

    def test_save_catalog(self):
        kinase1 = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase1, kinase2]
        my_catalog = Catalog(my_list_kinases)
        my_catalog.save_catalog("/Users/nicole/PycharmProjects/python-ii/test_save_catalog")
        new_catalog = Catalog.read_catalog("/Users/nicole/PycharmProjects/python-ii/test_save_catalog")
        self.assertEqual(len(new_catalog.get_proteins()), 2)
        self.assertEqual(new_catalog.get_proteins()[1].get_pdb_code(), "4LTR")
        self.assertEqual(new_catalog.get_proteins()[0].get_classification(), "transferasa")
        self.assertEqual(new_catalog.get_proteins()[0].get_organism(), "Homo sapiens")
        self.assertEqual(new_catalog.get_proteins()[1].get_year_deposited(), "2013-07-23")
        self.assertEqual(new_catalog.get_proteins()[1].get_manually_curated(), True)
        self.assertEqual(new_catalog.get_proteins()[1].get_atom_count(), "152")
        file = open("/Users/nicole/PycharmProjects/python-ii/test_save_catalog", "w")
        file.write("")
        file.close()

    # def test_add_protein(self):
    #     kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
    #     my_list_kinases = []
    #     my_catalog = Catalog(my_list_kinases)
    #     my_catalog.add_protein(kinase2)
    #     self.assertEqual(my_catalog.get_proteins(), [kinase2])

    def test_search_protein(self):
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        kinase1 = Protein("4LMR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase2, kinase1]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(my_catalog.search_proteins_pdb_code("4L"), [kinase2, kinase1])
        self.assertEqual(my_catalog.search_proteins_pdb_code("MMM"), [])
        self.assertEqual(my_catalog.search_proteins_pdb_code("4LMR"), [kinase1])

    def test_search_protein_classification(self):
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        kinase1 = Protein("4LMR", "transport h20", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase2, kinase1]
        my_catalog = Catalog(my_list_kinases)
        self.assertEqual(my_catalog.search_proteins_classification("transport"), [kinase2, kinase1])
        self.assertEqual(my_catalog.search_proteins_classification("MMM"), [])
        self.assertEqual(my_catalog.search_proteins_classification("transport h20"), [kinase1])

    def test_delete_protein(self):
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        kinase1 = Protein("4LMR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase2, kinase1]
        my_catalog = Catalog(my_list_kinases)
        my_catalog.delete_protein("4LMR")
        self.assertEqual(my_catalog.get_proteins(), [kinase2])
        my_catalog.delete_protein("4CCC")
        self.assertEqual(my_catalog.get_proteins(), [kinase2])
        self.assertTrue(my_catalog.delete_protein("4LTR"))
        self.assertFalse(my_catalog.delete_protein("4LTR"))

    def test_add_or_edit(self):
        kinase2 = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        kinase1 = Protein("4LMR", "transport h20", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        my_list_kinases = [kinase2]
        my_catalog = Catalog(my_list_kinases)
        my_catalog.add_or_edit(kinase1)
        self.assertEqual(my_catalog.get_proteins(), [kinase2, kinase1])
        kinase2_edited = Protein("4LTR", "transport protein", "Alkalilimnicola sapo", "2013-07-23", True, "152")
        my_catalog.add_or_edit(kinase2_edited)
        self.assertEqual(my_catalog.get_proteins(), [kinase2_edited, kinase1])
        self.assertEqual(kinase2.get_organism(),"Alkalilimnicola sapo")





