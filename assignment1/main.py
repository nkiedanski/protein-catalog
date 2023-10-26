# CLASS PROTEIN
from protein import Protein
from catalog import Catalog
# PROGRAM

FILE_PATH = "./catalog.txt"

catalog = Catalog.read_catalog(FILE_PATH)

running_program = True

while running_program:
    print("""*** Welcome to the Protein Catalog ***
    ---What do you want to do?
     1 – View the catalog
     2 – Search for a protein by PDB code
     3 – Search for a protein by name
     4 – Add or update a protein record
     5 – Delete a protein record
     0 – Exit the program""")
    activity = int(input("Please enter here the number: "))

    if activity == 1:
        print("*** Viewing the catalog ***")
        print(catalog)

    if activity == 2:
        search_pdb_code = str(input("Please write the protein's PDB code: ")).upper()
        proteins_found = catalog.search_proteins_pdb_code(search_pdb_code)
        catalog_found = Catalog(proteins_found)
        print(catalog_found)

    if activity == 3:
        search_name = str(input("Please write the protein's name: ")).lower()
        proteins_found = catalog.search_proteins_classification(search_name)
        catalog_found = Catalog(proteins_found)
        print(catalog_found)

    if activity == 4:
        pdb_code = str(input("Please write the protein's PDB code: ")).upper()
        classification = str(input("Please write the protein's name: ")).lower()
        organism = str(input("Please write the protein's organism: "))
        year_deposited = str(input("Please write year deposited: "))
        manually_curated = bool(input("Please write 'True' or 'False': "))
        atom_count = str(input("Please write atom count: "))
        protein_created = Protein(pdb_code, classification, organism, year_deposited, manually_curated, atom_count)
        catalog.add_or_edit(protein_created)
        print("Protein added/edited")

    if activity == 5:
        search_pdb_code = str(input("Please write the protein's PDB code you want to delete: ")).upper()
        deleted_successfully = catalog.delete_protein(search_pdb_code)
        if deleted_successfully:
            print("Protein deleted")
        else:
            print("This protein is not in the catalog")

    if activity == 0:
        should_save = str(input("Do you want to save changes before exit? - yes/no: ")).upper()
        if should_save == "YES":
            catalog.save_catalog(FILE_PATH)
        running_program = False
        print("Goodbye!")




