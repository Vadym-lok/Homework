import requests
from pprint import pprint
url = 'https://script.google.com/macros/s/AKfycbz4ZbYB5LZZy_IoOUPzgurffejA3mpTJu0gfpkDIVHniIWWAE6VodSraBLLXVO5lwvm/exec'

data = requests.get(url)

data_js = data.json()

the_cost_of_all = 0
the_cost_without_gluten = 0
for value in data_js['data']:
    the_cost_of_all += value['price']
    if value['contains gluten'] is False:
        the_cost_without_gluten += value['price']

pprint(the_cost_of_all)
pprint(the_cost_without_gluten)
