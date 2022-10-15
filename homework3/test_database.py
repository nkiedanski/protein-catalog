import unittest
from database import Database
from protein import Protein


class TestCatalog(unittest.TestCase):

    def test_retrieve_proteins(self):
        my_database = Database()
        alfa = Protein("3C49", "transferasa", "Homo sapiens","2008-01-29",True,"357")
        beta = Protein("3C48","transferasa","Homo sapiens","2004-01-29",True,"508")
        gama = Protein("4LTR","transport protein","Alkalilimnicola ehrlichii","2013-07-23",True,"152")
        list_proteins = [alfa, beta, gama]
        self.assertEqual(my_database.retrieve_proteins(), list_proteins)

    def test_retrieve_protein_id(self):
        my_database = Database()
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        list_proteins = [alfa]
        self.assertEqual(my_database.retrieve_protein_id("3C49"), list_proteins)




if __name__ == '__main__':
        unittest.main()