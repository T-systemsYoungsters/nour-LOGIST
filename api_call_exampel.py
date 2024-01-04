import requests
import json
proxies = {
   'http': 'http://sia-lb.telekom.de:8080/',
   'https': 'http://sia-lb.telekom.de:8080/',
   
}

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url, proxies=proxies)
    weather_data = response.json()
    
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Description: {weather_description}")
    else:
        print("City not found.")

with open('secret.json','r')as file:
    api_key = json.load(file)
   
city_name = "berlin"
get_weather(api_key.get('api_key'), city_name)