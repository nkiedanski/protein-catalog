import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import MinMaxScaler

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
scaler = MinMaxScaler()
x_low = merged_df[merged_df["category"] == "low"][["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                               "chlorides", "total sulfur dioxide", "density", "pH", "sulphates",
                                               "alcohol"]]
x_low_scaled = scaler.fit_transform(x_low.to_numpy())
x_low_scaled = pd.DataFrame(x_low_scaled)

x_mid = merged_df[merged_df["category"] == "mid"][["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                               "chlorides", "total sulfur dioxide", "density", "pH", "sulphates",
                                               "alcohol"]]
x_mid_scaled = scaler.fit_transform(x_mid.to_numpy())
x_mid_scaled = pd.DataFrame(x_mid_scaled)

x_high = merged_df[merged_df["category"] == "high"][["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                                 "chlorides", "total sulfur dioxide", "density", "pH", "sulphates",
                                                 "alcohol"]]
x_high_scaled = scaler.fit_transform(x_high.to_numpy())
x_high_scaled = pd.DataFrame(x_high_scaled)

# PLOT GRAPHS



# DE BARRAS
x = np.arange(len(x_low.columns))
height_low = x_low_scaled.mean()
height_mid = x_mid_scaled.mean()
height_high = x_high_scaled.mean()
# yerr = 1.96*x_low.std()/math.sqrt(len(x_low.index))
# yerr2 = 1.96*x_mid.std()/math.sqrt(len(x_mid.index))
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


ax = plt.axes()
plt.plot(x, height_low, linewidth=0.5, color="magenta", label="low category")
plt.plot(x, height_mid, linewidth=0.5, color="blue", label="mid category")
plt.plot(x, height_high, linewidth=0.5, color="green", label="high category")
ax.set_xticks(x)
ax.legend()
ax.set_xticklabels(x_low.columns.tolist(), fontsize=4.5)

# Adding title to ax and figure
plt.title("Wine variables per category", fontsize=10)
plt.xlabel("Wine variables")
plt.ylabel("Mean of wine variables +- std")
plt.show()
