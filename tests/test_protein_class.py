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

if __name__ == '__main__':
    unittest.main()