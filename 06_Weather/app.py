import requests 
from pprint import pprint
from datetime import datetime


LAT = 52.5244
LON = 13.4105

LANG = "de"
API_KEY = "c8c9804770ee1d3a436156f36382f09c"

CITY_NAME = "Berlin"
COUNTRY_CODE = "de"

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang={LANG}"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}&units=metric&lang={LANG}"



# Get the Data Response
respose = requests.get(URL)
data = respose.json()

pprint(data) 

temp = data["main"]["temp"]
description = data["weather"][0]["description"] 




sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]

# convert the UTC format to human readable format 
sunrise = datetime.utcfromtimestamp(sunrise).strftime('%H:%M:%S')
sunset = datetime.utcfromtimestamp(sunset).strftime('%H:%M:%S')


print(temp)
print(description)
print(sunrise)
print(sunset)