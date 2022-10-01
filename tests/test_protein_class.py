import unittest
from ..protein import Protein

# pdb_code, classification, organism, year_deposited, manually_curated, atom_count):

# Proteina 1
# Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
# Proteina 2
# Protein("4LTR", "transport protein", "Alkalilimnicola ehrlichii", "2013-07-23", True, "152")
# Proteina 3
# Protein("6BB5", "oxygen transpot", "Homo sapiens", "2017-10-16", False, "139")

# Proteina no valida por TypeError Manually Curated
# Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", 90, "357")

class TestProtein(unittest.TestCase):

    def test_initialize_protein_with_valid_manually_curated(self):
        self.assertTrue(isinstance(Protein("6BB5", "oxygen transpot", "Homo sapiens", "2017-10-16", False, "139"), Protein))

    def test_initialize_protein_with_invalid_manually_curated(self):
        try:
            Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", "45", "357")
            protein_created = True
        except TypeError:
            protein_created = False
        self.assertFalse(protein_created)

    def test_get_pdb_code_valid(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_pdb_code(),"3C49")

    def test_set_pdb_code_valid(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinasa.set_pdb_code("AJ78")
        self.assertEqual(kinasa.get_pdb_code(), "AJ78")

    def test_get_classification(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_classification(), "transferasa")

    def test_set_classification(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinasa.set_classification("kinasa")
        self.assertEqual(kinasa.get_classification(), "kinasa")

    def test_get_organism(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_organism(), "Homo sapiens")

    def test_set_organism(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinasa.set_organism("bacteria")
        self.assertEqual(kinasa.get_organism(), "bacteria")

    def test_get_year_deposited(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_year_deposited(), "2008-01-29")

    def test_set_year_deposited(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinasa.set_year_deposited("2008-01-31")
        self.assertEqual(kinasa.get_year_deposited(), "2008-01-31")

    def test_get_manually_curated(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_manually_curated(), True)

    def test_set_manually_curated(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        try:
            kinasa.set_manually_curated("89")
        except TypeError:
            pass
        self.assertEqual(kinasa.get_manually_curated(), True)

    def test_get_atom_count(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_atom_count(), "357")

    def test_get_atom_count(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        kinasa.set_atom_count("78")
        self.assertEqual(kinasa.get_atom_count(), "78")

    def test_max_spacing(self):
        kinasa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(kinasa.get_max_spacing(), 12)

    def test_turn_to_string(self):

        kinasa = Protein("3C", "tra", "Ho", "2", True, "357")
        self.assertEqual("3C   tra  Ho   2    True 357  ", kinasa.turn_to_string(5))

    def test_str_(self):

        kinasa = Protein("3C", "tra", "Ho", "2", True, "357")
        self.assertEqual("3C    tra   Ho    2     True  357   ", kinasa.__str__())

    def test_sort_proteins(self):
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "358")
        beta = Protein("3C48", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        list = [alfa, beta]
        list.sort()
        self.assertEqual(list, [beta, alfa])
        self.assertNotEqual(list, [alfa, beta])

    def test_eq__(self):
        alfa = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "358")
        beta = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertEqual(alfa, beta)
        gama = Protein("3C48", "transferasa", "Homo sapiens", "2008-01-29", True, "358")
        delta = Protein("3C49", "transferasa", "Homo sapiens", "2008-01-29", True, "357")
        self.assertNotEqual(gama, delta)


if __name__ == '__main__':
    unittest.main()

