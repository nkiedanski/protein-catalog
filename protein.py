

class Protein:
    def __init__(self, id, classification, organism, year_deposited, manually_curated, atom_count):
        self.__pdb_code = id
        self.__classification = classification
        self.__organism = organism
        self.__year_deposited = year_deposited
        if type(manually_curated) != bool:
            raise TypeError("Protein not valid. Manually curated value should be: True or False")
        self.__manually_curated = manually_curated
        self.__atom_count = atom_count

# getters and setter are defined
    def get_pdb_code(self):
        return self.__pdb_code

    def set_pdb_code(self, new_pdb_code):
        self.__pdb_code = new_pdb_code

    def get_classification(self):
        return self.__classification

    def set_classification(self, new_classification):
        self.__classification = new_classification

    def get_organism(self):
        return self.__organism

    def set_organism(self, new_organism):
        self.__organism = new_organism

    def get_year_deposited(self):
        return self.__year_deposited

    def set_year_deposited(self, new_year):
        self.__year_deposited = new_year

    def get_manually_curated(self):
        return self.__manually_curated

    def set_manually_curated(self, new_value):
        if type(new_value) != bool:
            raise TypeError("Value not valid. Manually curated value should be: True or False")
        self.__manually_curated = new_value

    def get_atom_count(self):
        return self.__atom_count

    def set_atom_count(self, new_ac):
        self.__atom_count = new_ac

# other methods

    def get_max_spacing(self):
        max_spacing = max(
            len(self.__pdb_code),
            len(self.__classification),
            len(self.__organism),
            len(self.__year_deposited),
            len(str(self.__manually_curated)),
            len(self.__atom_count)
        )
        return max_spacing

    def turn_to_string(self, spacing):
        string = self.__pdb_code.ljust(spacing) \
                 + self.__classification.ljust(spacing) \
                 + self.__organism.ljust(spacing) \
                 + self.__year_deposited.ljust(spacing) \
                 + str(self.__manually_curated).ljust(spacing) \
                 + self.__atom_count.ljust(spacing)

        return string

    def __str__(self):
        sep = self.get_max_spacing() + 2
        return self.turn_to_string(sep)

    def __lt__(self, other):
        result = False
        if other is not None and isinstance(other, Protein):
            result = self.__pdb_code < other.__pdb_code
            if self.__pdb_code == other.__pdb_code:
                result = self.__classification < other.__classification
                if self.__classification == other.__classification:
                    result = self.__organism < other.__organism
                    if self.__organism == other.__organism:
                        result = self.__year_deposited < other.__year_deposited
                        if self.__year_deposited == other.__year_deposited:
                            result = self.__atom_count < other.__atom_count
        return result

    def __eq__(self, other):
        result = False
        if other is not None:
            if isinstance(other, Protein):
                result = self.__pdb_code == other.__pdb_code
        return result

