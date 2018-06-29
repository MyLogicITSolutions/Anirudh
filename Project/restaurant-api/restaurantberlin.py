import pymongo
from pymongo import MongoClient
from requests import get
from bs4 import BeautifulSoup

url='http://www.lotus-restaurant-berlin.de/speisen/99/#Suppen'

# Lists to store the scraped data in
names = []
prices = []
descriptions = []
types = []
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
dish_container = html_soup.find_all('article')
dishType = html_soup.find('h1', class_ = 'section-title').text
price = 0
name= ''
for h1 in dish_container:
    item=h1.find('h1').text
    desc=h1.find('p').text
    item=item[1:]
    i=0
    for i in range(len(item)):
        if item[i].isnumeric():
            name = item[0:i]
            price = item[i:]
            names.append(name)
            prices.append(price)
            descriptions.append(desc)
            types.append(dishType)
            break

url='http://www.lotus-restaurant-berlin.de/speisen/vegetarian/#Vegetarisch'
# Lists to store the scraped data in
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
dish_container = html_soup.find_all('article')
dishType = html_soup.find('h1', class_ = 'section-title').text
price = 0
name= ''
for h1 in dish_container:
    item=h1.find('h1').text
    desc=h1.find('p').text
    item=item[2:]
    i=0
    for i in range(len(item)):
        if item[i].isnumeric():
            name = item[0:i]
            price = item[i:]
            names.append(name)
            prices.append(price)
            descriptions.append(desc)
            types.append(dishType)
            break

restaurantName = 'Lotus Restaurant'
restaurantAddress = 'Kantstrasse 70, 10627 Berlin'
restaurantEmail = 'info@lotus-restaurant-berlin.de'
restaurantPhone = '030 23948340'
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

