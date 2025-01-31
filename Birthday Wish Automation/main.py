##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import pandas
import datetime as dt 

date = dt.datetime.today()
dateMonth = date.month
dateDay = date.day

MY_EMAIL = "ommdevgoswami01@gmail.com"
MY_PASSWORD = "xozz sqdf dpvy lxqs"

birthday = pandas.read_csv("Birthday Wish Automation\\birthdays.csv")
birthday["month"] = pandas.to_numeric(birthday["month"], errors="coerce").astype("Int64")
birthday["day"] = pandas.to_numeric(birthday["day"], errors="coerce").astype("Int64")

for index, row in birthday.iterrows():
    if row["month"] == dateMonth and row["day"] == dateDay:
        # print("Today is a birthday!")
        letterList = ["Birthday Wish Automation\\letter_templates\\letter_1.txt", 
                    "Birthday Wish Automation\\letter_templates\\letter_2.txt",
                    "Birthday Wish Automation\\letter_templates\\letter_3.txt"]
        message = ""
        emailSelect = random.choice(letterList)
        try:
            with open(emailSelect, "r+") as file:
                letter = file.readlines()
                
                for _ in letter:
                    _ = _.replace("[NAME]", row["name"])
                    message += _
            
            with smtplib.SMTP("smtp.gmail.com", port=587) as birthdayWish:
                birthdayWish.starttls()
                birthdayWish.login(user=MY_EMAIL, password=MY_PASSWORD)
                birthdayWish.sendmail(from_addr=MY_EMAIL,
                                      to_addrs=row["email"],
                                      msg=f"Subject:Happy Birthday\n\n{message}"
                                    )
            
            print("Message Sent Successfully")
                
        except FileNotFoundError:
            print("Sorry, the letter template does not exist.")