import pandas as pd

# DataFrame = A tabular data structure with rows and columns. (2 Dimentional)
#             Similar to an Excel spreadsheet

data = {"Name":["Mohit", "Parvit", "Parul"],
        "Age": [30, 35, 28],

        }

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# Add a new column
df["Job"] = ["cook", "Intern", "Developer"]

# Add a new row
new_row = pd.DataFrame([{"Name": "Chirag", "Age": 18, "Job": "Ceo"},
                        {"Name": "Jonny", "Age": 49, "Job": "Plumber"}],
                       index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])

print(df)
print(df.loc["Employee 1"])