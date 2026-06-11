import pandas as pd

df = pd.read_json("data.json")
df = df.set_index("Name")

# SELECTION OF COLUMN
#print(df["Name"].to_string)
# print(df["Height"].to_string)
# print(df["Weight"].to_string)
# print(df[["Name","Height"]])

# SELECTION BY ROWS
# print(df)
# print(df.iloc[0])
print(df.loc["Pikachu"])
print(df.loc[["Pikachu", "Venusaur"]])
print(df.loc[["Pikachu", "Venusaur"],["Height", "Weight"]])
print("-------------------------------------")
print(df.loc["Pikachu":"Nidorina",["Height", "Weight"]])
#             From    : To
# print(df.iloc[20:30:2, 0:3])