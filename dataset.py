import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

pd.options.display.max_columns = 13
wine_red = pd.read_csv("winequality-red.csv", sep=";")
wine_white = pd.read_csv("winequality-white.csv", sep=";")

print("------------ Viewing Raw Dataframes ------------ ", "\n")
print("Red Wine Raw Dataset", "\n", wine_red)
print("White Wine Raw Dataset", "\n", wine_white)


print("------------ Description of Raw Dataframes ------------ ", "\n")
print("The shape of red wine file is: ", "rows: ", wine_red.shape[0], "columns: ", wine_red.shape[1], "\n"
      "The shape of white wine file is: ", "rows: ", wine_white.shape[0], "columns: ", wine_white.shape[1], "\n")
print("Is there any missing value in the red wine data?: ", wine_red.isnull().values.any(), "\n"
      "Is there any missing value in the white wine data?: ", wine_white.isnull().values.any(), "\n")
print("Are the same variables being measure?: ", wine_red.columns.values.tolist() == wine_white.columns.values.tolist())
print("**The wine variables are:** ", *wine_red.columns.values.tolist(), "\n", sep="\n", )


print("------------ Group Dataframes and Classify by Quality Category ------------ ", "\n")
wine_white["type"] = "white"
wine_red["type"] = "red"

merged_df = pd.concat([wine_red, wine_white], axis=0)
merged_df.reset_index(inplace=True, drop=True)

merged_df["category"] = None
merged_df.loc[merged_df.loc[:, "quality"] >= 7, "category"] = "high"
merged_df.loc[merged_df.loc[:, "quality"] < 7, "category"] = "mid"
merged_df.loc[merged_df.loc[:, "quality"] <= 3, "category"] = "low"
print("Complete Wine Dataset", "\n", merged_df, "\n")

# Saving new dataset
merged_df.to_csv("new_dataset.csv")


print("------------ Statistical Analysis ------------ ", "\n")
taste_variables = ["citric acid", "residual sugar", "density", "alcohol"]
quality_variables = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides",
                     "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]

stat_description_type = merged_df.groupby("type")[taste_variables].agg([np.mean, np.std])
stat_description_category = merged_df.groupby("category")[quality_variables].agg([np.mean, np.std])

print("Statistical description by type: red/white", "\n", stat_description_type, "\n")
print("Statistical description by category: low/mid/high", "\n", stat_description_category, "\n")

# Scaled dataset for graphs
scaler = MinMaxScaler()
merged_df_scaled = scaler.fit_transform(merged_df[quality_variables].to_numpy())
merged_df_scaled = pd.DataFrame(merged_df_scaled, columns=quality_variables)
merged_df_scaled_complete = pd.concat([merged_df_scaled, merged_df[["quality", "type", "category"]]], axis=1)


# PLOTTING GRAPH "WINE VARIABLES PER CATEGORY"
x_low = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "low"][quality_variables]
x_mid = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "mid"][quality_variables]
x_high = merged_df_scaled_complete[merged_df_scaled_complete["category"] == "high"][quality_variables]

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


# PLOTTING GRAPH "WINE VARIABLES PER TYPE"
x_red = merged_df_scaled_complete[merged_df_scaled_complete["type"] == "red"][taste_variables]
x_white = merged_df_scaled_complete[merged_df_scaled_complete["type"] == "white"][taste_variables]

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


# PLOTTING GRAPH "% OF QUALITY CATEGORY PER WINE TYPE"
graph_df_white = merged_df[merged_df["type"] == "white"]["category"].value_counts()
percentage_white = graph_df_white.values/graph_df_white.sum()*100
graph_df_red = merged_df[merged_df["type"] == "red"]["category"].value_counts()
percentage_red = graph_df_red.values/graph_df_red.sum()*100
# MODIFING FLOAT TO ONE DECIMAL PLACE ONLY
for index in range(0, len(percentage_white)):
    percentage_white[index] = round(percentage_white[index], 1)
    percentage_red[index] = round(percentage_red[index], 1)

category_names = graph_df_white.index.tolist()
results = {
    "white": percentage_white,
    "red": percentage_red
}
labels = list(results.keys())
data = np.array(list(results.values()))
# axis=1 because sum over columns for each of the 2 rows
data_cum = data.cumsum(axis=1)
# data.shape[1] returns de quantity of columns/labels/variables to indicate number of colores (samples) needed
category_colors = plt.colormaps['PRGn'](
    np.linspace(0, 0.77, data.shape[1]))

fig3 = plt.figure()
ax3 = plt.axes()
ax3.invert_yaxis()
ax3.xaxis.set_visible(False)

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    rects = ax3.barh(labels, widths, left=starts, height=0.45, align="center", label=colname, color=color)
    r, g, b, _ = color
    text_color = "white" if r * g * b < 0.1 else "black"
    ax3.bar_label(rects, label_type='center', color=text_color)
ax3.legend(ncol=len(category_names), loc="best", fontsize="small")
plt.title("% of Quality Category per Wine Type", fontsize=10)
plt.show()
