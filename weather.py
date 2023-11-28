import requests
import json
import constants
from datetime import datetime

# Class for town / city including name and lat/lng
class Location:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng

# Create tuple of supported locations. Lat / Long will be used in the API call to overcome the limitation
# that spaces in place names with spaces are not supported in the HTTP request.
locations = {
    Location('ldnp', 'Lake District National Park', 54.4609, -3.0886),
    Location('cc', 'Corfe Castle', 50.6395, -2.0566),
    Location('tc', 'The Cotswolds', 51.8330, -1.8433),
    Location('c', 'Cambridge', 52.2053, 0.1218),
    Location('b', 'Bristol', 51.4545, -2.5879),
    Location('o', 'Oxford', 51.7520, -1.2577),
    Location('n', 'Norwich', 52.6309, 1.2974),
    Location('s', 'Stonehenge', 51.1789, -1.8262),
    Location('wb', 'Watergate Bay', 50.4429, -5.0553),
    Location('bi', 'Birmingham', 52.4862, -1.8904)
}

# convert tuple to a dictionary to allow us to pick one location out
locations_by_key = {location.key: location for location in locations}

# Defining a class to store the weather data we are interested in
class WeatherData:
    def __init__(self, date, weather_main, description, min_temp, max_temp, icon):
        self.date = date
        self.weather_main = weather_main
        self.description = description
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.icon = icon


# Function to get the weather data and return it into an instance of a WeatherData class.
def get_weather_forecast(lat, lng, API_key):
    # requests API data using inputs
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?'
                        f'lat={lat}'
                        f'&lon={lng}'
                        f'&appid={API_key}'
                        f'&units=metric').json()


    # create empty array to store forecast
    weatherforecast = []

    # create iterable object to go through the 'daily' array in the returned API
    iter_object = iter(resp.get('daily'))
    while True:
        try:
            day = next(iter_object)
            # creates a WeatherData class and extracts the data from the response
            data = WeatherData(
                date=datetime.utcfromtimestamp(day.get('dt')).strftime('%d-%m-%Y'),
                weather_main=day.get('weather')[0].get('main'),
                description=day.get('weather')[0].get('description'),
                min_temp=round(day.get('temp').get('min'), 1),
                max_temp=round(day.get('temp').get('max'), 1),
                icon=day.get('weather')[0].get('icon')
            )
            weatherforecast.append(data)
        except StopIteration:
            break

    print(weatherforecast[3].date)
    #
    # data = WeatherData(
    #     date=datetime.utcfromtimestamp(resp.get('daily')[0].get('dt')).strftime('%d-%m-%Y'),
    #     weather_main=resp.get('daily')[0].get('weather')[0].get('main'),
    #     description=resp.get('daily')[0].get('weather')[0].get('description'),
    #     min_temp=round(resp.get('daily')[0].get('temp').get('min'), 1),
    #     max_temp=round(resp.get('daily')[0].get('temp').get('max'), 1),
    #     icon=resp.get('daily')[0].get('weather')[0].get('icon')
    # )
    # # print(resp.get('daily')[0].get('weather')[0].get('icon'))
    # print(data.date)
    # return data

# Exported function to be imported into another file
# def main(lat, lng):
#     weather_info = get_current_weather(lat, lng, constants.api_key_openweather)
#     return weather_info

get_weather_forecast(50.6395, -2.0566, constants.api_key_openweather)