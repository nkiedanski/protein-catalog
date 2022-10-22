import pandas as pd
from protein import Protein


class Database:

    def __init__(self):
        self.__df = pd.read_csv("proteins.csv", sep=";")

    def retrieve_proteins(self):
        list_proteins = []
        for row_index in range(self.__df.shape[0]):
            id = self.__df.iloc[row_index, 0]
            classification = self.__df.iloc[row_index, 1]
            organism = self.__df.iloc[row_index, 2]
            year_deposited = self.__df.iloc[row_index, 3]
            manually_curated = bool(self.__df.iloc[row_index, 4])
            atom_count = self.__df.iloc[row_index, 5]
            protein = Protein(id, classification, organism, year_deposited, manually_curated, atom_count)
            list_proteins.append(protein)
        return list_proteins

    def retrieve_protein_id(self, pdb_code):
        list_proteins = []
        if self.__df["--PDBcode--"].isin([pdb_code]).any():
            index_pdb_code = int(self.__df[self.__df["--PDBcode--"] == pdb_code].index.values)
            id = self.__df.iloc[index_pdb_code, 0]
            classification = self.__df.iloc[index_pdb_code, 1]
            organism = self.__df.iloc[index_pdb_code, 2]
            year_deposited = self.__df.iloc[index_pdb_code, 3]
            manually_curated = bool(self.__df.iloc[index_pdb_code, 4])
            atom_count = self.__df.iloc[index_pdb_code, 5]
            protein = Protein(id, classification, organism, year_deposited, manually_curated, atom_count)
            list_proteins.append(protein)
        return list_proteins

    # def retrieve_protein_id(self, pdb_code):
    #     list_proteins = []
    #     if self.__df["--PDBcode--"].isin([pdb_code]).any():
    #         index_pdb_code = int(self.__df[self.__df["--PDBcode--"] == pdb_code].index.values)
    #         id = self.__df.iloc[index_pdb_code, 0]
    #         classification = self.__df.iloc[index_pdb_code, 1]
    #         organism = self.__df.iloc[index_pdb_code, 2]
    #         year_deposited = self.__df.iloc[index_pdb_code, 3]
    #         manually_curated = bool(self.__df.iloc[index_pdb_code, 4])
    #         atom_count = self.__df.iloc[index_pdb_code, 5]
    #         protein = Protein(id, classification, organism, year_deposited, manually_curated, atom_count)
    #         list_proteins.append(protein)
    #     return list_proteins

    def retrieve_protein_classification(self, classification):
        list_proteins = []
        if self.__df["--Classification--"].isin([classification]).any():
            index_classification = self.__df[self.__df["--Classification--"] == classification].index.values.tolist()
            for index in index_classification:
                id = self.__df.iloc[index, 0]
                classification = self.__df.iloc[index, 1]
                organism = self.__df.iloc[index, 2]
                year_deposited = self.__df.iloc[index, 3]
                manually_curated = bool(self.__df.iloc[index, 4])
                atom_count = self.__df.iloc[index, 5]
                protein = Protein(id, classification, organism, year_deposited, manually_curated, atom_count)
                list_proteins.append(protein)
        return list_proteins

    def add_protein(self, protein):
        new_row = {"--PDBcode--": protein.get_pdb_code(), "--Classification--": protein.get_classification(),
                   "--Organism--": protein.get_organism(), "--YearDeposited--": protein.get_year_deposited(),
                   "--ManuallyCrurated--": protein.get_manually_curated(), "--AtomCount--": protein.get_atom_count()}
        self.__df = self.__df.append(new_row, ignore_index=True)
        self.__df.to_csv("proteins.csv", sep=";", index=False, mode="w")

    def delete_protein(self, protein):
        pdb_code = protein.get_pdb_code()
        index_pdb_code = int(self.__df[self.__df["--PDBcode--"] == pdb_code].index.values)
        self.__df = self.__df.drop(index_pdb_code)
        self.__df.to_csv("proteins.csv", sep=";", index=False, mode="w")

    def update_protein(self, protein):
        index_pdb_code = int(self.__df[self.__df["--PDBcode--"] == protein.get_pdb_code()].index.values)
        self.__df.iloc[index_pdb_code, 1] = protein.get_classification()
        self.__df.iloc[index_pdb_code, 2] = protein.get_organism()
        self.__df.iloc[index_pdb_code, 3] = protein.get_year_deposited()
        self.__df.iloc[index_pdb_code, 4] = protein.get_manually_curated()
        self.__df.iloc[index_pdb_code, 5] = protein.get_atom_count()
        self.__df.to_csv("proteins.csv", sep=";", index=False, mode="w")





