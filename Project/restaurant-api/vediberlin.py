import pymongo
from pymongo import MongoClient
from requests import get
from bs4 import BeautifulSoup

url='https://vedis.berlin/speisekarte/suppen'

# Lists to store the scraped data in
names = []
prices = []
descriptions = []
types = []
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
dish_container = html_soup.find_all('li', class_='food-menu-items-li')
dish_container1 = html_soup.find_all('div', class_='food-item-content')
dishType = 'suppen'
price = 0
name= ''
for h3 in dish_container:
    head = h3.find_all('h3')
    span1= h3.find_all('span', class_='fi-title')
    for i in span1:
        name= i.text
        names.append(name)
    span2= h3.find_all('span', class_='food-item-price')
    for k in span2:
        price = k.text
        prices.append(price)
for p in dish_container1:
    x = p.find_all('p')
    for j in x:
        desc= j.text
        descriptions.append(desc)
        types.append(dishType)

url='https://vedis.berlin/speisekarte/vegetarisch'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
dish_container = html_soup.find_all('li', class_='food-menu-items-li')
dish_container1 = html_soup.find_all('div', class_='food-item-content')
dishType = 'vegetarisch'
for h3 in dish_container:
    head = h3.find_all('h3')
    span1= h3.find_all('span', class_='fi-title')
    for i in span1:
        name= i.text
        names.append(name)
    span2= h3.find_all('span', class_='food-item-price')
    for k in span2:
        price = k.text
        prices.append(price)
for p in dish_container1:
    x = p.find_all('p')
    for j in x:
        desc= j.text
        descriptions.append(desc)
        types.append(dishType)
restaurantName = 'VEDIS INDIAN RESTAURANT'
restaurantAddress = 'Schönhauser Allee 142, 10437 Berlin'
restaurantEmail = 'info@vedis.berlin'
restaurantPhone = '+49(0)304485172'
import json

try:
    conn = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

db = conn.demo

collection = db.dishes

i=0
while i < len(names) :
    food = {'dishName': names[i],'Price': prices[i],'description':descriptions[i],'type':types[i],'restaurantName':restaurantName,'restaurantAddress':restaurantAddress,'restaurantEmail':restaurantEmail,'restaurantPhone':restaurantPhone}
    i=i+1
    print(json.dumps(food))
    r1 = collection.insert_one(food)
