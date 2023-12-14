import requests 


area = int(input("Enter the area: "))

URL = f"http://127.0.0.1:8000/predict?area={area}"

resposne = requests.get(URL)

data = resposne.json() 


print(data)