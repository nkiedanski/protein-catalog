from .protein import Protein
class Catalog:

    headers = ["--PDBcode--", "--Classification--", "--Organism--", "--YearDeposited--", "--ManuallyCrurated--",
               "--AtomCount--"]

    def __init__(self, proteins):
        for protein in proteins:
            if not isinstance(protein, Protein):
                raise TypeError("Catalog not valid. All elements should be proteins")
        self.__proteins = proteins

# getters and setters definition
    def get_proteins(self):
        return self.__proteins

    def set_proteins(self, updated_proteins):
        self.__proteins = updated_proteins

# other functions

    def max_spacing_for_all_proteins(self):
        max_spacing_each_protein = []
        for protein in self.__proteins:
            max_spacing = max(
               len(protein.get_pdb_code()),
               len(protein.get_classification()),
               len(protein.get_organism()),
               len(protein.get_year_deposited()),
               len(str(protein.get_manually_curated())),
               len(protein.get_atom_count())
            )
            max_spacing_each_protein.append(max_spacing)
        overall_max_spacing = max(max_spacing_each_protein)
        return overall_max_spacing

    def max_spacing_headers(self):
        i = 0
        max_space_header = 0
        while i < len(Catalog.headers):
            if len(Catalog.headers[i]) > max_space_header:
                max_space_header = len(Catalog.headers[i])
            i += 1
        return max_space_header

    def generate_headers(self):
        overall_max_spacing = max(self.max_spacing_headers(), self.max_spacing_for_all_proteins())
        headers_string = ""
        i = 0
        while i < len(Catalog.headers):
            headers_string = headers_string + Catalog.headers[i].ljust(overall_max_spacing) + " "
            i += 1
        return headers_string
