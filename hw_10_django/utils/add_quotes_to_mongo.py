import json
from bson.objectid import ObjectId

from pymongo import MongoClient

uri = "mongodb+srv://artemF_web16:wubmyw-bysroK-0fuwnu@cluster0.94vozhi.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client.web16_hw10

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
