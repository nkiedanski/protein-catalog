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
print("**The wine variables are:** ", *wine_red.columns.values.tolist(), "\n", sep="\n", )

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

taste_variables = ["citric acid", "residual sugar", "density", "alcohol"]
stat_description_type = merged_df.groupby("type")[taste_variables].agg([np.mean, np.std])
print("Statistical description by type: red/white", "\n", stat_description_type, "\n")

quality_variables = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides",
                     "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
stat_description_category = merged_df.groupby("category")[quality_variables].agg([np.mean, np.std])
print("Statistical description by category: low/mid/high", "\n", stat_description_category, "\n")

# Scaled dataset
scaler = MinMaxScaler()
merged_df_scaled = scaler.fit_transform(merged_df[quality_variables].to_numpy())
merged_df_scaled = pd.DataFrame(merged_df_scaled, columns=quality_variables)
merged_df_scaled_complete = pd.concat([merged_df_scaled, merged_df[["quality", "type", "category"]]], axis=1)
print("Complete Wine Dataset Scaled", "\n", merged_df_scaled_complete, "\n")


# GRAPHICS RELATED TO CATEGORY
x_low = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "low"][quality_variables]
x_mid = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "mid"][quality_variables]
x_high = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "high"][quality_variables]

# PLOT GRAPHS
fig = plt.figure()
x = np.arange(len(x_low.columns))
y_low = x_low.mean()
y_mid = x_mid.mean()
y_high = x_high.mean()
ax = plt.axes()
plt.plot(x, y_low, linewidth=0.5, color="magenta", label="low category")
plt.plot(x, y_mid, linewidth=0.5, color="blue", label="mid category")
plt.plot(x, y_high, linewidth=0.5, color="green", label="high category")
ax.set_xticks(x)
ax.legend()
ax.set_xticklabels(x_low.columns.tolist(), fontsize=4.5)
# Adding title to ax and figure
plt.title("Wine variables per category", fontsize=10)
plt.xlabel("Wine variables")
plt.ylabel("Mean of wine variables")
plt.show()


# GRAPHICS RELATED TO TYPE
x_red = merged_df_scaled_complete[merged_df_scaled_complete["type"] == "red"][taste_variables]
x_white = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "mid"][taste_variables]
# PLOT GRAPHS
fig2 = plt.figure()
x2 = np.arange(len(x_red.columns))
y_red = x_red.mean()
y_white = x_white.mean()
ax2 = plt.axes()
plt.plot(x2, y_red, linewidth=1, color="purple", label="red wine")
plt.plot(x2, y_white, linewidth=1, color="pink", label="white wine")
ax2.set_xticks(x2)
ax2.legend()
ax2.set_xticklabels(x_red.columns.tolist(), fontsize=4.5)
# Adding title to ax and figure
plt.title("Wine variables per type", fontsize=10)
plt.xlabel("Wine variables")
plt.ylabel("Mean of wine variables")
plt.show()

# GRAPHIC RELATED TO CATEGORY AND TYPE
x3 = np.arange(len(pregunta_2_2.index))
fig3 = plt.figure()
ax3 = plt.axes()
fig, ax = plt.subplots(figsize=(12,7))
ax.bar(x, height, yerr=yerr, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Media intención de voto +- desviación estándar')
ax.set_xticks(x)
ax.set_xticklabels(pregunta_2_2.index)
ax.set_title('Media intención de voto por grupo demográfico')
ax.yaxis.grid(True)
plt.tight_layout()
plt.show()

