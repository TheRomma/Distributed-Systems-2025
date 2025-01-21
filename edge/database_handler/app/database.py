from pymongo import MongoClient
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['metadata']
collection = db['videos']

def add_entry(link: str, title: str):
    filename = os.path.basename(link)
    entry = {"filename": filename, "title": title}
    collection.insert_one(entry)
    print(f"Added entry: {entry}")

def remove_entry(filename: str):
    result = collection.delete_one({"filename": filename})
    if result.deleted_count > 0:
        print(f"Removed entry with filename: {filename}")
    else:
        print(f"No entry found with filename: {filename}")
