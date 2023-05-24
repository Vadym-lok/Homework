import requests
from pprint import pprint
url = 'https://dummyjson.com/users'
response = requests.get(url)
data = response.json()
general_age = 0
average_age = 0
number_of_people = 0
for value in data['users']:
    products = value.get('hair')
    data_age = value.get('age')
    city_value = value.get('address')
    if products['color'] == 'Brown':
        number_of_people += 1
        general_age += data_age
        average_age = round(general_age / number_of_people, 1)
    if city_value['city'] == 'Louisville':
        pprint(city_value)

pprint(average_age)
