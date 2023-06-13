import json
from pprint import pprint
import requests

with open('homework.json', mode='r', encoding='utf-8') as json_file:
    new_json_file = json.load(json_file)
    for value in new_json_file:
        pprint(value)

url = "https://upload.wikimedia.org/wikipedia/commons/1/19/Europ%C3%A4ischer_Ziesel_in_Hockstellung.jpg"
url_1 = "https://ichef.bbci.co.uk/news/800/cpsprodpb/6C7E/production/_98847772_60e395f3-f84e-4215-8626-0b977b85e838.jpg"
responce = requests.get(url)
responce_2 = requests.get(url_1)
with open('picture.jpg', mode='wb') as picture_files:
    picture_files.write(responce.content)

with open('picture_2.jpg', mode='wb') as picture_files:
    picture_files.write(responce_2.content)
