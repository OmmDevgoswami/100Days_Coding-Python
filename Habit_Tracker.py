"""ALERT NOTE:  The API might not work as expected always. It has a 25% chance of success on each call. So 'updation' function added below might have some bugs.
Repeated calls might work. But it is not guaranteed. So, please be patient and try again later if it doesn't work. Thank you!!"""

import requests
import datetime as dt

KEY = "ommi0103"
USER = "omm"

AUTHENTICATION = {
    "X-USER-TOKEN": KEY
}

PIXELA_USER = {
    "token" : KEY,
    "username" : USER,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# newUser = requests.post(url = "https://pixe.la/v1/users", json = PIXELA_USER)
# print(newUser.text)
### For User Creation : One Time Process

GRAPH_DATA = {
    "id" : "graph01",
    "name": "Coding Tracking",
    "unit": "hour",
    "type": "int",
    "color": "ajisai",
    "timezone": "Asia/Kolkata"
}
    
# createGraph = requests.post(url = f"https://pixe.la/v1/users/{USER}/graphs", json = GRAPH_DATA, headers = AUTHENTICATION)
# print(createGraph.text)
### For Graph Creation : One Time Process

def pixelaCount(count):
    today = dt.datetime.today()
    datePattern = today.strftime("%Y%m%d")
    count = str(count)
    
    PATTERN_DATA = {
        "date": datePattern,
        "quantity": count
    }
    
    addPattern = requests.post(url = f"https://pixe.la/v1/users/{USER}/graphs/graph01", json = PATTERN_DATA, headers = AUTHENTICATION)
    print(addPattern.text)
    
def dailyRecorder():
    print("Greetings Buddy!!\nHow was you day today? Hope you had a great day!!")
    print("Let's record your hours of coding today!!")
    count = int(input("How many hours did you code today? "))
    while(True):
        if count == 0:
            print("Today must have been a rought day!! No worries, you can always start fresh tomorrow!!")
            print("Have a good rest today")
            break
        else:
            print(f"Woahh!! That's fabulous!! You have coded for {count} hours today!!")
            pixelaCount(count)
            cont = input("Do you want to add more hours? (Y/N) ").lower()
            if cont == "y":
                today = dt.datetime.today()
                datePattern = today.strftime("%Y%m%d")
                getCurrent = requests.get(url = f"https://pixe.la//v1/users/{USER}/graphs/graph01/{datePattern}", headers = AUTHENTICATION)
                getCurrent.raise_for_status()
                curValue = getCurrent.json()
                count = int(input("How many hours did you code today? ")) 
                updateVal = int(curValue["quantity"]) + count
                check = requests.put(url=f"https://pixe.la/v1/users/{USER}/graphs/graph01/{datePattern}", json={"quantity": str(updateVal)}, headers=AUTHENTICATION)
                print(check.text)
                print("Updated Successfully!!")
            else:
                print("Great Job Buddy!! See you tomorrow!!")
                break
            
    
dailyRecorder()
