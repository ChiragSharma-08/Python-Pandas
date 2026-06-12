import pandas as pd

# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevent data.
#                 ~75% of work dont with pandas is data cleaning

df = pd.read_csv("data.csv")

#1. Drop irrelevent columns
# df = df.drop(columns = ["Legendary", "No"])

#2. Handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

#3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass":"GHASS", 
#                                    "Fire": "AAG", 
#                                    "Water": "PANI", 
#                                    "Bug": "KEEDA", 
#                                    "Electric": "BIJLI", 
#                                    "Normal": "AAM"})

#4. Standardize text 
# df["Name"] = df["Name"].str.lower()

#5. Fix data type
# df["Legendary"] = df["Legendary"].astype(bool)

#6. Remove duplicate values
df = df.drop_duplicates()


print(df.to_string())