# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:12:21 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""
import mongo
from entity import Report

class DAO(object):
    
    def __init__(self):
        self._col = mongo.get_collection("reports")
    
    def insertReport(self,report):
        self._col.insert(report)
        
    def fetchAllReports(self):
        reports = []
        cur = self._col.find()
        for doc in cur:
            reports.append(doc)
        return reports
    
    
if __name__ == "__main__":
    
    d = DAO()
    print d.fetchAllReports()
    
        
    
        

