# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 13:12:21 2014

@author: Samarth Bhargav
@author: Karthik Srivatsa
"""


class Report(object):   

    @staticmethod
    def toJson(report):
        r = {}
        r["title"] = report.title
        r["desc"] = report.desc
        r["location"] = report.location
        r["difficulty"] = report.difficulty
        r["pic"] = report.pic
        r["time"] = report.time
        return r
    
    def fromJson(values):
        report = Report()
        report._title = values["title"]
        report._difficulty = values["difficulty"]
        report._time = values["time"]
        report._desc = values["desc"]
        report._location = values["location"]
        report._pic = values["pic"]
        return report

    
    def __init__(self,values = None):
        if values == None :
            self._title = None
            self._difficulty = None
            self._time = None
            self._desc = None
            self._location = {}
            self._location["lat"] = None
            self._location["long"] = None
            self._pic = None
        else:
            self = Report.fromJson()
    
     # properties
    
    @property
    def title(self):
        return self._title
        
    @property
    def difficulty(self):
        return self._difficulty
        
    @property
    def desc(self):
        return self._desc
        
    @property
    def time(self):
        return self._time
        
    @property
    def location(self):
        return self._location

    @property
    def pic(self):
        return self._pic        
    
    # setters
    @title.setter
    def title(self, value):
        self._title = value
    
    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value
    
    @time.setter
    def time(self, value):
        self._time = value
    
    @desc.setter
    def desc(self, value):
        self._desc = value
    
    @location.setter
    def location(self, value):
        self._location = value
    
    @pic.setter
    def pic(self, value):
        self._pic = value
    
           
if __name__ == "__main__":
    rep = Report()
    rep.title = "Hell"
    print rep.title