import pandas as pd

df = pd.read_json("data.json")

# SELECTION OF COLUMN
#print(df["Name"].to_string)
# print(df["Height"].to_string)
# print(df["Weight"].to_string)
print(df[["Name","Height"]])