from .protein import Protein
class Catalog:
    def __init__(self, proteins):
        for protein in proteins:
            if isinstance(protein, Protein) == False:
                raise TypeError("Catalog not valid. All elements should be proteins")
        self.proteins = proteins

