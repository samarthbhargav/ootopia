# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 16:14:37 2014

@author: karthik
"""

from pygeocoder import Geocoder

class MapApi(object):
    
    def __init__(self):
        self._result = None

    def reverse_geocode(self,lat,lon):
        result = Geocoder.reverse_geocode(lat,lon)
        address = []
        addr =  result.formatted_address.split(",")
        for component in addr:
            component = str(component)
            component = component.strip()
            address.append(component)
        return address
            
if __name__ == "__main__":
    g = MapApi()
    print g.reverse_geocode(12.971290, 77.508385)