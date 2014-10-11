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
        r["description"] = report.desc
        r["location"] = report.location
        r["difficulty"] = report.difficulty
        r["imageData"] = report.pic
        r["time"] = report.time     
        if report.id is not None:
            r["id"] = report.id
        r["status"] = report.status        
        return r
    
    @staticmethod
    def fromJson(values):
        report = Report()
        if "title" in values:
            report._title = values["title"]
        if "difficulty" in values:
            report._difficulty = values["difficulty"]
        if "time" in values:
            report._time = values["time"]
        if "description" in values:
            report._desc = values["description"]
        if "location" in values:
            report._location = values["location"]
        if "imageData" in values:
            report._pic = values["imageData"]
        if "status" in values:
            report._status = values["status"]
        if "_id" in values:
            report._id = str(values["_id"])        
        return report

    
    def __init__(self):        
        self._title = None
        self._difficulty = None
        self._time = None
        self._desc = None
        self._location = {
            "lat" : None,
            "long" : None, 
            "address": []                
        }
        self._location["lat"] = None
        self._location["long"] = None
        self._pic = None
        self._id = None
        self._status = None
    
     # properties

    @property
    def status(self):
        return self._status
    
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

    @property
    def latitude(self):
        if self._location is not None and "lat" in self._location:
            return self._location["lat"]
        else:
            return None
    
        
    @property
    def longitude(self):
        if self._location is not None and "long" in self._location:
            return self._location["long"]
        else:
            return None
    
    @property
    def address(self):
        if self._location is not None and "address" in self._location:
            return self._location["address"]
        else:
            return None
        
    @property
    def id(self):
        return self._id
        
    @status.setter
    def status(self, value):
        self._status = value
    
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
    
    @id.setter
    def id(self, value):
        self._id = value
          
    @address.setter
    def address(self, value):        
        self._location["address"] = value
        
    def __str__(self):        
        return "\n".join("{}: {}".format(k, v) for k,v in vars(self).items())
        
if __name__ == "__main__":
    rep = Report()
    rep.title = "Hell"
    print rep.title
