from pymongo import MongoClient

def get_database_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["mydatabase"]