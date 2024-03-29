from catalog import Catalog
import matplotlib.pyplot as plt


def visualization(list_of_proteins, catalog_operator):
    headers = catalog_operator.generate_headers()
    s = headers
    s = s + "\n"
    for each_protein in list_of_proteins:
        s = s + each_protein.turn_to_string(catalog_operator.overall_max_spacing()) + "\n"
    return s


def graph_pie_chart_classification(catalog_operator):
    labels = catalog_operator.graph_group_by_classification()[0]
    quantities = catalog_operator.graph_group_by_classification()[1]
    fig1, ax1 = plt.subplots()
    ax1.pie(quantities, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Quantity of Proteins(%) by Classification")
    plt.show()


def graph_plot_year(catalog_operator):
    values = catalog_operator.graph_group_by_year()
    x = [int(i) for i in values[0]]
    y = values[1]
    plt.plot(x, y, "bd--")

    plt.xlabel("year deposited")
    plt.ylabel("No. of Proteins")
    plt.title("No. Proteins by Year Deposited")
    plt.show()


catalog = Catalog()

running_program = True

while running_program:
    print("""*** Welcome to the Protein Catalog ***
    ---What do you want to do?
     1 – View all proteins
     2 – Search for a protein by PDB code
     3 – Search for a protein by classification
     4 – Add or update a protein record
     5 – Delete a protein record
     6 - Show Graph Quantity of Proteins by Classification
     7 - Show Graph Quantity of Proteins by Year Deposited
     0 – Exit the program""")
    activity = int(input("Please enter here the number: "))

    if activity == 1:
        print("*** Viewing all proteins ***")
        print(catalog)

    if activity == 2:
        search_pdb_code = str(input("Please write the protein's PDB code: ")).upper()
        proteins_found = catalog.retrieve_proteins_by_id(search_pdb_code)
        print("*** Viewing proteins found ***")
        print(visualization(proteins_found, catalog))

    if activity == 3:
        search_name = str(input("Please write the protein's classification: ")).lower()
        proteins_found = catalog.retrieve_proteins_by_classification(search_name)
        print("*** Viewing proteins found ***")
        print(visualization(proteins_found, catalog))

    if activity == 4:
        pdb_code = str(input("Please write the protein's PDB code: ")).upper()
        classification = str(input("Please write the protein's name: ")).lower()
        organism = str(input("Please write the protein's organism: "))
        year_deposited = str(input("Please write year deposited: "))
        manually_curated = bool(input("Please write 'True' or 'False': "))
        atom_count = str(input("Please write atom count: "))
        catalog.update_protein_if_exist_add_it_otherwise(pdb_code, classification, organism, year_deposited,
                                                         manually_curated, atom_count)
        print("Protein added/edited")

    if activity == 5:
        search_pdb_code = str(input("Please write the protein's PDB code you want to delete: ")).upper()
        catalog.delete_protein_if_exists(search_pdb_code)
        print("Done!")

    if activity == 6:
        graph_pie_chart_classification(catalog)

    if activity == 7:
        graph_plot_year(catalog)

    if activity == 0:
        running_program = False
        print("Goodbye!")




