

class Protein:
    def __init__(self, pdb_code, classification, organism, year_deposited, manually_curated, atom_count):
        self.pdb_code = pdb_code
        self.classification = classification
        self.organism = organism
        self.year_deposited = year_deposited
        if type(manually_curated) != bool:
            raise TypeError("Protein not valid. Manually curated value should be: True or False")
        self.manually_curated = manually_curated
        self.atom_count = atom_count

