import unittest
import pandas as pd

from database import Database
from protein import Protein
from catalog import Catalog


class TestCatalog(unittest.TestCase):

    def setUp(self):
        data = {"--PDBcode--": pd.Series(["3C49", "3C48", "4LTR"]),
                "--Classification--": pd.Series(["transferasa", "transferasa", "transport protein"]),
                "--Organism--": pd.Series(["Homo sapiens", "Homo sapiens", "Alkalilimnicola ehrlichii"]),
                "--YearDeposited--": pd.Series(["2008-01-29", "2004-01-29", "2013-07-23"]),
                "--ManuallyCrurated--": pd.Series(["True", "True", "True"]),
                "--AtomCount--": pd.Series(["357", "508", "152"])}
        base_dataframe = pd.DataFrame(data)
        base_dataframe.to_csv("proteins.csv", sep=";", index=False, mode="w")

    def test_add_protein_no_addition(self):
        my_catalog = Catalog()
        result = my_catalog.add_protein_if_not_exist("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(result, False)

    def test_add_protein_addition(self):
        my_catalog = Catalog()
        result = my_catalog.add_protein_if_not_exist("NICOLE", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(result, True)

    def test_retrieve_proteins(self):
        my_catalog = Catalog()
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        beta = Protein("3C48", "transferasa", "Homo sapiens", "2004-01-29", True, "508")
        gama = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
        list_proteins = [alfa, beta, gama]
        self.assertEqual(my_catalog.retrieve_proteins(), list_proteins)

    def test_update_protein_exist(self):
        my_catalog = Catalog()
        my_catalog.update_protein_if_exist_add_it_otherwise("3C49", "kinase", "Homo sapiens", "2008-01-29", False,
                                                            "357")
        updated_protein = Protein("3C49", "kinase", "Homo sapiens", "2008-01-29", False, "357")
        self.assertEqual(my_catalog.retrieve_proteins()[0], updated_protein)

    def test_update_not_exists_addition(self):
     my_catalog = Catalog()
     my_catalog.update_protein_if_exist_add_it_otherwise("NICOLE", "kinase", "Homo sapiens", "2008-01-29", False,
                                                         "357")
     alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
     beta = Protein("3C48", "transferasa", "Homo sapiens", "2004-01-29", True, "508")
     gama = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
     new_protein = Protein("NICOLE", "kinase", "Homo sapiens", "2008-01-29", False, "357")
     list_proteins = [alfa, beta, gama, new_protein]
     self.assertEqual(my_catalog.retrieve_proteins(), list_proteins)

if __name__ == '__main__':
    unittest.main()
