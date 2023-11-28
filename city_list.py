# List of cities supported to be replaced by SQL statement
cities_list = ['Lake District National Park', 'Corfe Castle', 'The Cotswolds', 'Cambridge', 'Bristol',
                   'Oxford', 'Norwich', 'Stonehenge', 'Watergate Bay', 'Birmingham']

def extract_cities(string):
    detected_cities = []
    total_num = len(cities_list)
    for i in range(total_num):
        city = cities_list[i]
        if city in string:
            detected_cities.append(city)
    return detected_cities
