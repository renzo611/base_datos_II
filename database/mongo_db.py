import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_SCHEMA = os.getenv("MONGO_SCHEMA")
MONGO_PORT = os.getenv('MONGO_PORT')

def get_database():
 
   CONNECTION_STRING = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_SCHEMA}"
 
   client = MongoClient(CONNECTION_STRING)
 
   return client[MONGO_SCHEMA]
  
mongo_client = get_database()