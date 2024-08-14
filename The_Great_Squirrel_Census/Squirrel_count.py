import pandas

squirrel_count = pandas.read_csv("The_Great_Squirrel_Census\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = 0
cinnamon_count = 0
black_count = 0
for _ in squirrel_count["Primary Fur Color"]:
    if _ == "Gray":
        gray_count += 1
    elif _ == "Cinnamon":
        cinnamon_count += 1
    elif _ == "Black":
        black_count += 1
print (f"NCP has {gray_count} Gray Coloured Squirrels")
print (f"NCP has {cinnamon_count} Cinnamon Coloured Squirrels")
print (f"NCP has {black_count} Black Coloured Squirrels")

count = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(count)
data.to_csv("The_Great_Squirrel_Census\\squirrelcount.csv")