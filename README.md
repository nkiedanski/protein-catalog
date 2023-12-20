# python-ii

Introduction:

course: python-ii 2022 (msc bioinformatics)

final assignments: 
- assignment 1: protein catalog
- assignment 2: analysis, cleaning and reports on a dataset
- assignment 3: putting it all together

language: 
- python 3.9
  
packages:
- pandas
- numpy
- matplotlib
- scikit-learn
  
## Asignment 1: protein catalog

Create a program catalog.py for managing a protein catalog, made up of a number of functions

• The main function of the program (entry-point of its execution) will invoke an interactive function that provides the user with the following functionalities:
  1. Visualization of the catalog, showing proteins in alphabetical order
  2. Search for proteins by partial name/PDB code (this may return more than one result)
  3. Addition/editing of a protein passing all of its data
  4. Deletion of a protein based on its name or PDB code
  5. Exit from the program with the possibility of saving or not the modified catalog
     
• Each protein entry will have (at least) the following data fields:

    • PDBcode: unique identifier
    • Classification
    • Organism
    • YearDeposited
    • ManuallyCurated: true/false
    • AtomCount

• Files associated:
  - Homework_1.docx --> summary of the modeling and implementation choices made
  - main.py --> the main body with the instructions that enable it to run. The main imports the Class Protein from protein.py file and the class Catalog from the catalog.py file
  - protein.py --> it contains the Protein Class with all of its methods
  - catalog.py -->  it contains the Catalog Class with all of its methods
  - catalog.txt -->  the file containing the catalog to be read from, and where the catalog is saved.
    
    
## Asignment 2: analysis, cleaning and reports on a dataset

Datasets used where downloaded from:  https://archive.ics.uci.edu/ml/index.php

• Files associated:
  - Homework_2.docx --> summary of the modeling and implementation choices made
  - dataset.py --> main program with analysis and reports
  - winequality-red.csv --> original dataset
  - winequality-white.csv --> original dataset
  - new_dataset.csv --> cleaned dataset

## Asignment 3: putting it all together

Develop an interactive, object-oriented application for managing a "database" of biological entities.

The application should follow the three-tier architecture.

• The data layer of the application will be managed via a dataset handled as a Pandas Dataframe and provide the functionalities such as Create, Read, Update, Delete (CRUD) over the underlying data

• The logic layer will be built by classes and will aggregate the CRUD functionalities

• The presentation layer will provide a textual interface to interact with the program

• Files associated:
  - Homework_3.docx --> summary of the modeling and implementation choices made
  - protein.py --> it contains the Protein Class with all of its methods
  - database.py --> it refers to the Data Layer, where the Database Class was defined with all of its methods.
  - catalog.py --> it refers to the Logic Layer, where a Catalog Class was defined with all of its methods.
  - main.py --> it refers to the Presentation Layer, where the main program is and some related functions were defined.
  - proteins.csv --> the dataset created/modified in .CSV format

 




    

  
