import requests

API_KEY = "58217517b8f16a20bee437d00e75c3b9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200: #200 - ok or successful
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(data["main"]["temp"] - 273.15, 2)
    far = round( ((data["main"]["temp"] - 273.15) * (9/5))+ 32, 2)

    print("Weather: " + weather)
    print("Temperature (F): ", far)
    print("Temperature (C): ", temp)
    
else:
    print("An error occured.")

