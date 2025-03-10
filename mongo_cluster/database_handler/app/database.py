from pymongo import MongoClient
import os

#Connect to metadata database.
client = MongoClient(os.getenv("MONGO_SERVICE", 'mongodb://mongodb-service:27017/'))
db = client['metadata']
collection = db['videos']

#Functions for adding and removing entries.

def add_entry(link: str, title: str):
    filename = os.path.basename(link)
    if collection.find_one({"filename": filename}):
        print(f"Entry with filename '{filename}' already exists.")
        return
    entry = {"origin": link, "filename": filename, "title": title}
    collection.insert_one(entry)
    print(f"Added entry: {entry}")

def remove_entry(filename: str):
    if not collection.find_one({"filename": filename}):
        print(f"No entry found with filename: {filename}")
        return
    result = collection.delete_one({"filename": filename})
    if result.deleted_count > 0:
        print(f"Removed entry with filename: {filename}")
    else:
        print(f"Failed to remove entry with filename: {filename}")
