from .protein import Protein


class Catalog:
    headers = ["--PDBcode--", "--Classification--", "--Organism--", "--YearDeposited--", "--ManuallyCrurated--",
               "--AtomCount--"]

    def __init__(self, proteins):
        for protein in proteins:
            if not isinstance(protein, Protein):
                raise TypeError("Catalog not valid. All elements should be proteins")
        self.__proteins = proteins
        self.__filepath = None

    # getters and setters definition
    def get_proteins(self):
        return self.__proteins

    def set_proteins(self, updated_proteins):
        self.__proteins = updated_proteins

    def get_filepath(self):
        return self.__filepath

    def set_filepath(self, new_filepath):
        self.__filepath = new_filepath

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

    def read_catalog(filepath):
        file = open(filepath, "r")
        lines = file.readlines()
        proteins = []
        for line in lines:
            s = line.replace("\n", "").split("|")
            protein = Protein(s[0], s[1], s[2], s[3], bool(s[4]), s[5])
            proteins.append(protein)
        file.close()
        new_catalog = Catalog(proteins)
        new_catalog.set_filepath(filepath)
        return new_catalog

    def save_catalog(self, filepath):
        file = open(filepath, "w")
        for i in range(0, len(self.__proteins)):
            protein = self.__proteins[i]
            string = protein.get_pdb_code() + "|" + protein.get_classification() + "|" + protein.get_organism() + "|" + \
                     str(protein.get_year_deposited()) + "|" + str(protein.get_manually_curated()) + "|" + \
                     str(protein.get_atom_count())
            if i < len(self.__proteins)-1:
                string = string + "\n"
            file.write(string)
        file.close()

    def add_protein(self, protein):
        self.__proteins.append(protein)


