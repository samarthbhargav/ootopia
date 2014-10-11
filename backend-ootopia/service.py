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
        self._dao.insert_report(report)
    
    def fetch_all(self):
        reports = self._dao.fetch_all_reports()
        return { "results" : reports }
    
    def get_report(self, Id):
        return self._dao.get(Id)


if __name__ == "__main__":
    service = ReportService()
    
    print service.fetch_all()
    

