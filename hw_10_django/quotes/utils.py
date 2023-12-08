from pymongo import MongoClient
import sqlite3


def get_mongodb():
    uri = "mongodb+srv://artemF_web16:wubmyw-bysroK-0fuwnu@cluster0.94vozhi.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    try:
        db = client.web16_hw10
    except Exception as e:
        print(e)

    return db

