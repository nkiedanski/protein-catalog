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






