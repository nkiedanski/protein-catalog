import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

pd.options.display.max_columns = 13
print("------------ download ------------ ", "\n")
wine_red = pd.read_csv("winequality-red.csv", sep=";")
print("Wine Red dataset", "\n", wine_red)
wine_white = pd.read_csv("winequality-white.csv", sep=";")
print("Wine White dataset", "\n", wine_white)

print("------------ analysis ------------ ", "\n")
print("The shape of red wine file is: ", "rows: ", wine_red.shape[0], "columns: ", wine_red.shape[1], "\n",
      "The shape of white wine file is: ", "rows: ", wine_white.shape[0], "columns: ", wine_white.shape[1], "\n")

print("Is there any missing value in the red wine data?: ", wine_red.isnull().values.any(), "\n",
      "Is there any missing value in the white wine data?: ", wine_white.isnull().values.any(), "\n")

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

stat_description_type = merged_df.groupby("type")[["citric acid", "residual sugar", "density", "pH", "alcohol"]].\
    agg([np.mean, np.std])
print("Statistical description by type: red/white", "\n", stat_description_type, "\n")

stat_description_category = merged_df.groupby("category")[["fixed acidity", "volatile acidity", "citric acid",
                                                           "residual sugar", "chlorides", "total sulfur dioxide",
                                                           "density", "pH", "sulphates", "alcohol"]].agg([np.mean, np.std])
print("Statistical description by category: low/mid/high", "\n", stat_description_category, "\n")



# GRAPHICS RELATED TO CATEGORY
x_low = merged_df[merged_df["category"] == "low"][["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                               "chlorides", "total sulfur dioxide", "density", "pH", "sulphates",
                                               "alcohol"]]
x_mid = merged_df[merged_df["category"] == "mid"][["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                               "chlorides", "total sulfur dioxide", "density", "pH", "sulphates",
                                               "alcohol"]]
# x_high = merged_df[merged_df["category"] == "high"][["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
#                                                 "chlorides", "total sulfur dioxide", "density", "pH", "sulphates",
#                                                 "alcohol"]]
# DE BARRAS
x = np.arange(len(x_low.columns))
height = x_low.mean()
height2 = x_mid.mean()
# yerr = 1.96*x_low.std()/math.sqrt(len(x_low.index))
# yerr2 = 1.96*x_mid.std()/math.sqrt(len(x_mid.index))
#
# fig, ax = plt.subplots(figsize=(12,12))
# ax.bar(x, height, yerr=yerr, align='center', alpha=0.5, ecolor='black', capsize=10)
# ax.bar(x, height2, yerr=yerr2, align='center', alpha=0.5, ecolor='black', capsize=10)
# ax.set_ylabel("Mean of wine variables +- std")
# ax.set_xticks(x)
# ax.set_xticklabels(x_low.columns.tolist())
# ax.set_title("Wine variables per category")
# ax.yaxis.grid(True)
# plt.tight_layout()
# plt.show()

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# xp2 = np.array([0, 3, 7, 8])
# yp2 = np.array([5, 7, 8, 10])
# plt.plot(xpoints, ypoints, xp2, yp2
#  marker = "D",
#  linestyle = "dotted"
# ,
#  linewidth = "4.2",
#  color = "#ff0000")
# plt.show()


#fig = plt.figure()
ax = plt.axes()
# x = np.linspace(0, 10, 1000)
# Ploteamos en el axe actual 4 curvas diferentes
# Dibujamos los senos en rojo y los cosenos en azul
plt.plot(x, height, color='red')
plt.plot(x, height2, color='blue')
ax.set_xticks(x)
ax.set_xticklabels(x_low.columns.tolist())

# Le ponemos un tìtulo y tìtulos a los ejes, por supuesto
plt.title("Wine variables per category")
plt.xlabel("Wine variables")
plt.ylabel("Mean of wine variables +- std")
plt.show()
