# Weather

- Create an account in openweathermap.org and create an API key
- Get the current weather for three cities [Berlin, Aachen, Stuttgart]
- Store the received reponses for each city in a JSON file
- Store some of the received response fields in SQLite DB 



# Data Schema
### Table 1 : "city" 
1. ID
2. cityname


### Table 2: "weather" 
1. ID 
2. FK_cityID : Foreign Key of  the city 
3. Description EN
4. Description DE
5. Temperature: in c
6. temp_min
7. temp_max


# Project Coding suggestion
- Scriptwise
- Functionalwise
- Modulewise
- OOP
