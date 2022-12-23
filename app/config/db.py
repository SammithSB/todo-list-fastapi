import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

conn = MongoClient(os.environ.get("MONGO_URI"))
