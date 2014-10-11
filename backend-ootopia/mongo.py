# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:12:21 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""


from config import config
import pymongo



def get_collection(collection_name):
    mongo_client = pymongo.MongoClient(host=config.mongo_host, port=config.mongo_port)
    db = mongo_client[config.mongo_db]
    if config.mongo_username is not None:
        db.authenticate(config.mongo_username, password=config.mongo_password)
    return db[collection_name]



if __name__ == "__main__":
    coll = get_collection("Monkey")
    coll.insert({"as": "as"})