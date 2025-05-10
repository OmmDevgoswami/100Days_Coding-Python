# with open ("Pandas Revise\weather_data.csv", "r") as file:
#     file_content = file.readlines()
#     for context in file_content:
#         print(context.strip("\n"))

# import csv

# with open ("Pandas Revise/weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temepratureData = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temepratureData)
#     file.seek(0)
#     for content in data:
#         print(content)

import pandas as pd

file = pd.read_csv("Pandas Revise/weather_data.csv")
print(file)
# print(file.to_dict())

# print(file["temp"].to_list())

# Average_temp = sum(file["temp"])/len(file["temp"])
# Average_temp = file["temp"].mean()
# print(f"Average Temperature recored: {Average_temp}")

# Max_temp = file["temp"].max()
# print(f"Maximum Temperature recored: {Max_temp}")

# max_row = file[file["temp"] == file["temp"].max()]
# print(max_row)

# monday = file[file["day"] == "Monday"]
# celcius_to_fahrenheit = (monday.temp * 9/5) + 32
# print(f"Monday's temperature in Fahrenheit: {celcius_to_fahrenheit}")
print()

new_data = {
    "Students" : ["A", "B", "C"],
    "Scores" : [56, 76, 89],
    "Location" : ["Delhi", "Mumbai", "Kolkata"],
    "Weather" : ["Sunny", "Rainy", "Cloudy"]
}

data = pd.DataFrame(new_data)
print(data)
data.to_csv("Pandas Revise/new_data.csv", index=False)