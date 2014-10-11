# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:12:21 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""
import mongo
from entity import Report
from bson.objectid import ObjectId
import re

class DAO(object):
    
    def __init__(self):
        self._col = mongo.get_collection("Report")
    
    def insert_report(self,report):
        self._col.insert(Report.toJson(report))
        
    def fetch_all_reports(self):
        reports = []
        cur = self._col.find()
        for doc in cur:
            #doc["id"] = str(doc["_id"])
            #del doc["_id"]
            reports.append(Report.fromJson(doc))
        return reports
    
    def get(self, Id):
        rep = self._col.find_one({"_id":ObjectId(Id)})
        if rep is None:
            return None
        else:
            return Report.fromJson(rep)
    
    def fetch_report_with_address(self, address):
        reps = []
        for doc in self._col.find({"location.address": re.compile(".*{}.*".format(address), re.IGNORECASE)}):
            reps.append(Report.fromJson(doc))
        return reps
        
    def update_field(self, Id, field_name, new_value):
        self._col.update({"_id" : ObjectId(Id)}, { "$set": { field_name: new_value } }) 
        
if __name__ == "__main__":
    
    d = DAO()
    print d.fetch_all_reports()    
    print d.fetch_report_with_address("india")
    
        
    
        

