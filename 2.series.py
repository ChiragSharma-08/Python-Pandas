import pandas as pd

#Series = A Pandas 1-Dimensional labeled array that can hold any data type
#         Think of it like a single column in a spreadsheet(1-Dimentional)

data = [100, 103,  104]

series = pd.Series(data)
series = pd.Series(data, index = ["a", "b", "c"])

print(series)