# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:12:21 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""
import mongo

class DAO(object):
    
    def __init__(self):
        self._col = mongo.get_collection("Report")
    
    def insert_report(self,report):
        self._col.insert(report)
        
    def fetch_all_reports(self):
        reports = []
        cur = self._col.find()
        for doc in cur:
            doc["id"] = str(doc["_id"])
            del doc["_id"]
            reports.append(doc)
        return reports
    
    def get(self, Id):
        return self._col.find_one({"_id":Id})
        
if __name__ == "__main__":
    
    d = DAO()
    print d.fetchAllReports()
    
        
    
        

