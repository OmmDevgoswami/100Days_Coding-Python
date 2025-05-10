import pandas as pd

data = pd.read_csv("Pandas Revise\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours = data["Primary Fur Color"].dropna().unique()

details = {
    "Fur Colour" : colours,
    "Count" : [data["Primary Fur Color"].to_list().count(colour) for colour in colours]
}
new_data = pd.DataFrame(details)
print(new_data)
new_data.to_csv("Pandas Revise/squirrel_count.csv", index=False)
