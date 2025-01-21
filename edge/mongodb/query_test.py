import pymongo 
   
# establishing connection 
# to the database
client = pymongo.MongoClient("mongodb://localhost:27017/") 
   
# Database name 
db = client["metadata"] 
   
# Collection name 
col = db["videos"] 
 
# if we don't want to print id then pass _id:0
for x in col.find({}, {"_id":0, "title": 1, "filename": 1 }): 
    print(x)
