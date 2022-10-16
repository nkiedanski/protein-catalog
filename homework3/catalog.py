from protein import Protein
from database import Database


class Catalog:

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

    def update_protein_if_exist_add_it_otherwise(self, pdb_code, classification, organism, year_deposit, manually_curated, atom_count):
        protein = Protein(pdb_code, classification, organism, year_deposit, manually_curated, atom_count)
        if protein in self.__database.retrieve_protein_id(pdb_code):
            self.__database.update_protein(protein)
        else:
            self.__database.add_protein(protein)





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
        overall_max_spacing = max(max_spacing_each_protein, default=0)
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
        self.__proteins.sort()
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

    def add_or_edit(self, search_protein):
        if search_protein not in self.__proteins:
            self.__proteins.append(search_protein)
        else:
            position = self.__proteins.index(search_protein)
            protein = self.__proteins[position]
            protein.set_classification(search_protein.get_classification())
            protein.set_organism(search_protein.get_organism())
            protein.set_year_deposited(search_protein.get_year_deposited())
            protein.set_manually_curated(search_protein.get_manually_curated())
            protein.set_atom_count(search_protein.get_atom_count())

    def search_proteins_pdb_code(self, pdb_code):
        proteins_found = []
        for protein in self.__proteins:
            if protein.get_pdb_code().startswith(pdb_code):
                proteins_found.append(protein)
        return proteins_found

    def search_proteins_classification(self, name):
        proteins_found = []
        for protein in self.__proteins:
            if protein.get_classification().startswith(name):
                proteins_found.append(protein)
        return proteins_found

    def delete_protein(self, pdb_code):
        protein_deleted = False
        for protein in self.__proteins:
            if protein.get_pdb_code() == pdb_code:
                self.__proteins.remove(protein)
                protein_deleted = True
        return protein_deleted
