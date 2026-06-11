# Filtering = Keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("data.csv")

# tall_pokemon = df[df["Height"]>= 2]
# heavy_pokemon = df[df["Height"]>= 2]
# legendary_pokemon = df[df["Height"]>= 2]

water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"] == "Water")]

fire_flying_pokemon = df[(df["Type1"] == "Fire") &
                         (df["Type2"] == "Flying")
                         ]

print(fire_flying_pokemon)