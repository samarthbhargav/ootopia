# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:13:58 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""
from dao import DAO

class ReportService(object):
    
    def __init__(self):
        self._dao = DAO()
    
    def insert(self,report):
        self._dao.insertReport(report)
    
    def fetchAll(self):
        reports = self._dao.fetchAllReports()
        return { "results" : reports }
        


if __name__ == "__main__":
    service = ReportService()
    
    print service.fetchAll()
    

