import pandas

data = pandas.read_csv("Pandas_Intro - Weather_Info\\weather_data.csv")
print (data)
print ("\nTemperature\n",data["temp"])

#Note
# Series : Each column of Data in a csv file
# DataFrame : Entire Table of  Data in a csv file

print()
dict_ex = data.to_dict()
print (dict_ex)
print()
list_ex = data["temp"].to_list()
print (list_ex)
print ()
average_temp = 0
# for _ in list_ex:
#     average_temp += _
# average_temp /= len(list_ex)
average_temp = data["temp"].mean()
print (f"Average Temperature Across the Week: {average_temp}")
print()
max = data["temp"].max()
print (f"Max Temperature {max}\n")
print (data[data.temp == max])
print ()
monday = data[data.day == "Monday"]
temperature = (monday.temp)*(9/5)+32
print (temperature)
print ()
weather_report = {
    "Delhi": {
        "temperature": "34°C",
        "humidity": "60%",
        "condition": "Partly Cloudy"
    },
    "Mumbai": {
        "temperature": "29°C",
        "humidity": "80%",
        "condition": "Rain Showers"
    },
    "Bengaluru": {
        "temperature": "25°C",
        "humidity": "70%",
        "condition": "Clear Sky"
    },
    "Kolkata": {
        "temperature": "32°C",
        "humidity": "75%",
        "condition": "Thunderstorms"
    },
    "Chennai": {
        "temperature": "33°C",
        "humidity": "85%",
        "condition": "Hazy"
    }
}

report  = pandas.DataFrame(weather_report)
new_report = report.to_csv("Pandas_Intro - Weather_Info\\new_report.csv")
weather = pandas.read_csv("Pandas_Intro - Weather_Info\\new_report.csv")
print (weather)