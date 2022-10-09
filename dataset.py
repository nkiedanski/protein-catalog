
import pandas as pd
import numpy as np

wine_red = pd.read_csv("winequality-red.csv", sep=";")
print("Wine Red dataset", "\n", wine_red)
wine_white = pd.read_csv("winequality-white.csv", sep=";")
print("Wine White dataset", "\n", wine_white)

print("The shape of red wine file is: ", "rows: ", wine_red.shape[0], "columns: ", wine_red.shape[1], "\n"
      "The shape of white wine file is: ", "rows: ", wine_white.shape[0], "columns: ", wine_white.shape[1], "\n")

print("Is there any null value in the red wine data?: ", wine_red.isnull().values.any(), "\n"
      "Is there any null value in the white wine data?: ", wine_white.isnull().values.any(), "\n")

print("Are the same variables being measure?: ", wine_red.columns.values.tolist() == wine_white.columns.values.tolist())
print("The wine variables are: ", *wine_red.columns.values.tolist(), sep="\n")
