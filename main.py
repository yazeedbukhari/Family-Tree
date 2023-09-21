from pymongo import MongoClient
import private

client = MongoClient(private.cluster)

print(client.list_database_names())

db = client.Trees

print(db.list_collection_names())

person1 = {"name": "Yazeed", "ID": 1,
            "dad": "Ahmad", "dID": 2, 
            "mom": "Amirah", "mID": 3}

names = db.names

# result = names.insert_one(person1)

# result = names.insert_many(persons)

from bson.objectid import ObjectId  #to access objectId directly instead of through name or my id thing
#result = names.find_one({'_id': ObjectId('650bc31672a7d85ce9582e6e')}) # returns the first thing with whatever specific you searched for
#results = names.find() #returns a cursor object which is probably a pointer that has a list of all objects with the thing you serached for
                        #once this cursor is used in any operation, it is "consumed", ie gone. cant be used again, must call find again
#print(list(results)) 
#for result in results:
    #print(result)

# print(names.count_documents({"name": "Yazeed"})) #obvious. returns documents with specified tag use {} for empty requirements ie everything

results = names.find({}).sort("name") #sorts by whatever metric you want
for result in results:
    print(result)
#result = names.delete_one({}) #deletes smth using tag or smth
#names.delete_many({})

#result = names.update_one({thing to define objects that get changed}, {"$set": {key of thing and changed mapped value}}) 
#result = names.update_one({"name": "Yazeed"}, {"$set": {"mID": "Amirah"}}) #if use $unset instead of $set and put none instead of key-value pair we delete key
                                                                            #alternatively if you use $set with a new key it will input a new key-value pair
#result = names.update_many({thing to change}, {what to change to})



