
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

wine_red = pd.read_csv("winequality-red.csv", sep=";")
wine_white = pd.read_csv("winequality-white.csv", sep=";")

print("The shape of red wine file is: ", wine_red.shape, "\n"
      "The shape of white wine file is: ", wine_white.shape)

print("Is there any null value in the red wine data?: ", wine_red.isnull().values.any(), "\n"
      "Is there any null value in the white wine data?: ", wine_white.isnull().values.any())



