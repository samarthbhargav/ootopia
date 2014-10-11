# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:13:58 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""
from dao import DAO
from entity import Report
from geocoder import MapApi

class ReportService(object):
    mapAPI = MapApi()
    
    def __init__(self):
        self._dao = DAO()
    
    def insert(self,report):
        report = Report.fromJson(report)
        if report.latitude is not None and report.longitude is not None:
            report.address = ReportService.mapAPI.reverse_geocode(report.latitude, report.longitude)        
            
        id_ = self._dao.insert_report(report)
        if report.pic is not None and len(report.pic) != 0:
            img = report.pic.decode('base64')
            with open('static/{}.jpg'.format(id_), 'wb') as imgfile:
                imgfile.write(img)
        
    
    def fetch_all(self):
        reports = self._dao.fetch_all_reports()
        return { "results" : [ Report.toJson(report) for report in reports] }
    
    def get_report(self, Id):
        rep = self._dao.get(Id)
        if rep is not None:
            return Report.toJson(rep)
        else:
            return None

    def get_reports_by_location(self, location):
        reports = self._dao.fetch_report_with_address(location)
        return { "results" : [ Report.toJson(report) for report in reports] }

    def update_status(self, Id, new_status):
        self._dao.update_field(Id, "status", new_status)
        
if __name__ == "__main__":
    service = ReportService()
    
    print service.fetch_all()
    

