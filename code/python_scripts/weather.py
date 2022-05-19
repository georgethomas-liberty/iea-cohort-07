import requests

SECRET_KEY = "1d8c58ed1d54f96f939e706c788650f1"

lat, long = (43.2175066, -70.858064)

url = "https://api.darksky.net/forecast/{key}/{lat},{long}".format(
    key=SECRET_KEY, lat=lat, long=long
)

response = requests.get(url)
# print(url)
# print(response)
# print(dir(response))

forecast_data = response.json()
# print(forecast_data)

# from pprint import pprint
# print((forecast_data)

time = forecast_data["currently"]["time"]
temp = forecast_data["currently"]["temperature"]
# print(time, temp)

today = forecast_data["daily"]["data"][0]

print(
    "Today's Temps for 03869 - High: {high}, Low: {low}".format(
        high=today["temperatureHigh"], low=today["temperatureLow"]
    )
)
