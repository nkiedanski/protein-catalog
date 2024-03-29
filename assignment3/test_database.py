import unittest

import pandas as pd

from database import Database
from protein import Protein


class TestDatabase(unittest.TestCase):
    def setUp(self):
        data = {"--PDBcode--": pd.Series(["3C49", "3C48", "4LTR"]),
                "--Classification--": pd.Series(["transferasa", "transferasa", "transport protein"]),
                "--Organism--": pd.Series(["Homo sapiens", "Homo sapiens", "Alkalilimnicola ehrlichii"]),
                "--YearDeposited--": pd.Series(["2008-01-29", "2004-01-29", "2013-07-23"]),
                "--ManuallyCrurated--": pd.Series(["True", "True", "True"]),
                "--AtomCount--": pd.Series(["357", "508", "152"])}
        base_dataframe = pd.DataFrame(data)
        base_dataframe.to_csv("proteins.csv", sep=";", index=False, mode="w")

    def tearDown(self):
        data = {"--PDBcode--": pd.Series(["3C49", "3C48", "4LTR"]),
                "--Classification--": pd.Series(["transferasa", "transferasa", "transport protein"]),
                "--Organism--": pd.Series(["Homo sapiens", "Homo sapiens", "Alkalilimnicola ehrlichii"]),
                "--YearDeposited--": pd.Series(["2008-01-29", "2004-01-29", "2013-07-23"]),
                "--ManuallyCrurated--": pd.Series(["True", "True", "True"]),
                "--AtomCount--": pd.Series(["357", "508", "152"])}
        base_dataframe = pd.DataFrame(data)
        base_dataframe.to_csv("proteins.csv", sep=";", index=False, mode="w")

    def test_retrieve_proteins(self):
        my_database = Database()
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        beta = Protein("3C48", "transferasa", "Homo sapiens", "2004-01-29", True, 508)
        gama = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, 152)
        list_proteins = [alfa, beta, gama]
        self.assertEqual(my_database.retrieve_proteins(), list_proteins)

    def test_retrieve_protein_id(self):
        my_database = Database()
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        list_proteins = [alfa]
        self.assertEqual(my_database.retrieve_protein_id("3C49"), list_proteins)

    def test_retrieve_protein_classification(self):
        my_database = Database()
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        beta = Protein("3C48", "transferasa", "Homo sapiens", "2004-01-29", True, 508)
        list_proteins = [alfa, beta]
        self.assertEqual(my_database.retrieve_protein_classification("transferasa"), list_proteins)

    def test_add_protein(self):
        my_database = Database()
        alfa = Protein("NIC", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        my_database.add_protein(alfa)
        self.assertEqual(Database().retrieve_protein_id("NIC"), [alfa])

    def test_add_protein_modify_dataset(self):
        my_database = Database()
        alfa = Protein("NIC", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        my_database.add_protein(alfa)
        new_database = Database()
        self.assertEqual(new_database.retrieve_protein_id("NIC"), [alfa])

    def test_delete_protein(self):
        my_database = Database()
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        beta = Protein("3C48", "transferasa", "Homo sapiens", "2004-01-29", True, 508)
        gama = Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, 152)
        my_database.delete_protein(alfa.get_pdb_code())
        list_proteins = [beta, gama]
        self.assertEqual(Database().retrieve_proteins(), list_proteins)

    def test_update_protein(self):
        my_database = Database()
        alfa_new = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, 400)
        my_database.update_protein(alfa_new)
        retrieved_list = Database().retrieve_protein_id("3C49")
        self.assertEqual(retrieved_list[0].get_pdb_code(), "3C49")
        self.assertEqual(retrieved_list[0].get_classification(), "transferasa")
        self.assertEqual(retrieved_list[0].get_organism(), "Homo sapiens")
        self.assertEqual(retrieved_list[0].get_year_deposited(), "2008-01-29")
        self.assertEqual(retrieved_list[0].get_manually_curated(), True)
        self.assertEqual(retrieved_list[0].get_atom_count(), 400)

    def test_graph_group_by_classification(self):
        labels = ['transferasa', 'transport protein']
        quantities = [2, 1]
        self.assertEqual(Database().graph_group_by_classification(), [labels, quantities])

    def test_graph_group_by_year(self):
        alfa = Protein("3C55", "transferasa", "Homo sapiens", "2008-01-29", True, 357)
        x = ["2004", "2008", "2013"]
        y = [1, 2, 1]
        Database().add_protein(alfa)
        self.assertEqual(Database().graph_group_by_year(), [x, y])


if __name__ == '__main__':
    unittest.main()
