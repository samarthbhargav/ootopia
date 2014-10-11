# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:12:21 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""


_config = {
   "mongo-db" : "Ootopia",
   "mongo-username" : None,
   "mongo-password": None,
   "mongo-port" : 27017,
   "mongo-host": "localhost"
}




class Config(object):
    
    @property
    def mongo_db(self):
        return _config["mongo-db"]
    
    @property
    def mongo_username(self):
        return _config["mongo-username"]
        
    @property
    def mongo_password(self):
        return _config["mongo-password"]
        
    @property
    def mongo_port(self):
        return _config["mongo-port"]
    
    @property
    def mongo_host(self):
        return _config["mongo-host"]
        
        
config = Config()