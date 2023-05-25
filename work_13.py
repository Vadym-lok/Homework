import requests
from pprint import pprint
url = 'https://dummyjson.com/users?limit=100'
response = requests.get(url)
data = response.json()
users_data = data['users']
general_age = 0
average_age = 0
number_of_people = 0
for value in users_data:
    data['limit'] = 100
    hair_color = value.get('hair')
    data_age = value.get('age')
    city_value = value.get('address')
    city_data = city_value.get('city')
    if hair_color['color'] == 'Brown':
        number_of_people += 1
        general_age += data_age
    if city_data == 'Louisville':
        pprint(value)
average_age = round(general_age / number_of_people, 1)

pprint(average_age)
