from pymongo import MongoClient
import time
import os

def generate_html():
    #Connect to the metadata storage and query all videos.
    client = MongoClient(os.getenv("MONGO_SERVICE", 'mongodb://mongodb-service:27017/'))
    db = client['metadata']
    collection = db['videos']

    #Creates a simple html document to be displayed.
    html_content = "<html><body>\n"
    for video in collection.find():
        title = video['title']
        filename = video['filename']
        html_content += f'<a href="{filename}">{title}</a><br>\n'
    html_content += "</body></html>"

    with open('videos/index.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    while True:
        generate_html()
        time.sleep(int(os.getenv("SLEEP_INTERVAL", "60")))  #The interval between frontend rebuilds. Adjust the interval as needed
