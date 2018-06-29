import pymongo
from pymongo import MongoClient
from requests import get
from bs4 import BeautifulSoup

url = 'https://www.gablenz-eck-lieferservice.de/speisekarte-haehnchen'

# Lists to store the scraped data in
names = []
prices = []
descriptions = []
types = []
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
dish_container = html_soup.find_all('tr', class_ = 'article_bgcolora')
dishType = 'haehnchen'
for container in dish_container:
    span = container.find_all('span', class_ = 'article_name')
    span1 = container.find_all('span', class_ = 'description')
    td = container.find_all('td', class_ = 'prbox_bg_1 price_td_1')
    j=0
    for  i in span:
        if(j == 0):
            name = i.text
            names.append(name)
            j=j+1
    i=0
    for  j in span1:
        if(i == 0):
            description = j.text
            descriptions.append(description)
            i=i+1
    for row in td:
        meta = row.find_all('meta')
        title = row.find("meta", itemprop="price")
        prices.append(title["content"])
        types.append(dishType)
        
restaurantName = 'Gablenz Eck'
restaurantAddress = 'Bernhardstraße 112, 09126 Chemnitz'
restaurantEmail = 'info@gablenz-life-service.de'
restaurantPhone = '0371-56071134'

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


