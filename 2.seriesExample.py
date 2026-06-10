import pandas as pd

calories = {"Day1":1750, "Day2":2100, "Day3": 1700}

series = pd.Series(calories)

series.loc["Day3"] += 500

print(series)

print(series[series>=2000])