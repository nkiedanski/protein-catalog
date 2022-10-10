import pandas as pd
import numpy as np

pd.options.display.max_columns = 13
print("------------ download ------------ ", "\n")
wine_red = pd.read_csv("winequality-red.csv", sep=";")
print("Wine Red dataset", "\n", wine_red)
wine_white = pd.read_csv("winequality-white.csv", sep=";")
print("Wine White dataset", "\n", wine_white)

print("------------ analysis ------------ ", "\n")
print("The shape of red wine file is: ", "rows: ", wine_red.shape[0], "columns: ", wine_red.shape[1], "\n",
      "The shape of white wine file is: ", "rows: ", wine_white.shape[0], "columns: ", wine_white.shape[1], "\n")

print("Is there any null value in the red wine data?: ", wine_red.isnull().values.any(), "\n",
      "Is there any null value in the white wine data?: ", wine_white.isnull().values.any(), "\n")

print("Are the same variables being measure?: ", wine_red.columns.values.tolist() == wine_white.columns.values.tolist())
print("The wine variables are: ", *wine_red.columns.values.tolist(), "\n", sep="\n", )

print("------------ cleaning ------------ ", "\n")

wine_white["type"] = "white"
wine_red["type"] = "red"
merged_df = pd.concat([wine_red, wine_white], axis=0)
merged_df.reset_index(inplace=True, drop=True)

merged_df["category"] = None

merged_df.loc[merged_df.loc[:, "quality"] >= 7, "category"] = "high"
merged_df.loc[merged_df.loc[:, "quality"] < 7, "category"] = "mid"
merged_df.loc[merged_df.loc[:, "quality"] <= 3, "category"] = "low"

print("Complete Wine Dataset", "\n", merged_df, "\n")

stat_description_type = merged_df.groupby("type")[["citric acid", "residual sugar", "density", "pH", "alcohol"]]. \
    agg([np.mean, np.std])
print(stat_description_type)

stat_description_category = merged_df.groupby("category")[["citric acid", "residual sugar", "density", "pH", "alcohol"]].agg([np.mean, np.std])
print(stat_description_category)