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
            max_spacing = protein.get_max_spacing()
            max_spacing_each_protein.append(max_spacing)
        overall_max_spacing = max(max_spacing_each_protein)
        return overall_max_spacing

    def max_spacing_headers(self):
        max_space_header = 0
        for header in Catalog.headers:
            if len(header) > max_space_header:
                max_space_header = len(header)
        return max_space_header

    def __overall_max_spacing__(self):
        overall_max_spacing = max(self.max_spacing_headers(), self.max_spacing_for_all_proteins()) + 2
        return overall_max_spacing

    def generate_headers(self):
        headers_string = ""
        for header in Catalog.headers:
            headers_string = headers_string + header.ljust(self.__overall_max_spacing__())
        return headers_string

    def __str__(self):
        s = self.generate_headers()
        s = s + "\n"
        for protein in self.__proteins:
            s = s + protein.turn_to_string(self.__overall_max_spacing__()) + "\n"
            return s
