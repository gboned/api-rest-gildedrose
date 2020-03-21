# Conectar la app a BBDD mongo local

from pymongo import MongoClient
from mongoengine import *
import dns
from models import Item
from pprint import pprint
from collections import OrderedDict

# conectar con MongoDB
client = MongoClient('mongodb+srv://admin:12345@cluster0-ln2gy.mongodb.net/test?retryWrites=true&w=majority')
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# obteniendo una bbdd
db = client.ollivanders

# Getting a Collection
collection = db.inventario

# mongoengine: how to connect to our instance of mongod:
# db.connect.ollivanders
connect('ollivanders', 'default', host='localhost')

# adding data
def initdb():
    inventario = [["+5 Dexterity Vest", 10, 20],
                    ["Aged Brie", 2, 0],
                    ["Elixir of the Mongoose", 5, 7],
                    ["Sulfuras, Hand of Ragnaros", 0, 80],
                    ["Sulfuras, Hand of Ragnaros", -1, 80],
                    ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
                    ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
                    ["Backstage passes to a TAFKAL80ETC concert", 5, 49],
                    # ["Conjured Mana Cake", 3, 6]
                    ]

    for product in inventario:
        item = Item(name=product[0])
        item.sell_in = product[1]
        item.quality = product[2]
        post = {"name":item.name, "sell_in":item.sell_in, "quality":item.quality}
        collection.save(post)
        pprint(post)
    # item.save()
# collection.insert_one(post)
# pprint(post)
initdb()
