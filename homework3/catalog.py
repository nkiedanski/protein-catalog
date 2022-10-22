from protein import Protein
from database import Database


class Catalog:
    headers = ["--PDBcode--", "--Classification--", "--Organism--", "--YearDeposited--", "--ManuallyCrurated--",
               "--AtomCount--"]

    def __init__(self):
        self.__database = Database()

    def add_protein_if_not_exist(self, pdb_code, classification, organism, year_deposit, manually_curated, atom_count):
        protein = Protein(pdb_code, classification, organism, year_deposit, manually_curated, atom_count)
        if protein not in self.__database.retrieve_protein_id(pdb_code):
            self.__database.add_protein(protein)
            return True
        else:
            return False

    def retrieve_proteins(self):
        return self.__database.retrieve_proteins()

    def retrieve_proteins_by_id(self, pdb_code):
        return self.__database.retrieve_protein_id(pdb_code)

    def retrieve_proteins_by_classification(self, classification):
        return self.__database.retrieve_protein_classification(classification)

    def update_protein_if_exist_add_it_otherwise(self, pdb_code, classification, organism, year_deposit, manually_curated, atom_count):
        protein = Protein(pdb_code, classification, organism, year_deposit, manually_curated, atom_count)
        if protein in self.__database.retrieve_protein_id(pdb_code):
            self.__database.update_protein(protein)
        else:
            self.__database.add_protein(protein)

    def delete_protein_if_exists(self, pdb_code):
        if len(self.__database.retrieve_protein_id(pdb_code)) is not 0:
            self.__database.delete_protein(pdb_code)


    # other functions

    def max_spacing_for_all_proteins(self):
        max_spacing_each_protein = []
        for protein in self.retrieve_proteins():
            max_spacing = protein.get_max_spacing()
            max_spacing_each_protein.append(max_spacing)
        overall_max_spacing = max(max_spacing_each_protein, default=0)
        return overall_max_spacing

    def max_spacing_headers(self):
        max_space_header = 0
        for header in Catalog.headers:
            if len(header) > max_space_header:
                max_space_header = len(header)
        return max_space_header

    def overall_max_spacing(self):
        overall_max_spacing = max(self.max_spacing_headers(), self.max_spacing_for_all_proteins()) + 2
        return overall_max_spacing

    def generate_headers(self):
        headers_string = ""
        for header in Catalog.headers:
            headers_string = headers_string + header.ljust(self.overall_max_spacing())
        return headers_string

    def __str__(self):
        s = self.generate_headers()
        s = s + "\n"
        self.retrieve_proteins().sort()
        for protein in self.retrieve_proteins():
            s = s + protein.turn_to_string(self.overall_max_spacing()) + "\n"
        return s

    def graph_group_by_classification(self):
        return self.__database.graph_group_by_classification()

    def graph_group_by_year(self):
        return self.__database.graph_group_by_year()