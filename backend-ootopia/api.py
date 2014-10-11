# -*- coding: utf-8 -*-
"""

Exposes the APIs required for the Application

Created on Sat Oct 11 14:03:15 2014

@author: Samarth Bhargav
"""

from flask import Flask
from flask.ext import restful
from flask import request
from functools import wraps
from config import config
from service import ReportService
 
app = Flask(__name__)
api = restful.Api(app)



def basic_authentication():
    """
    Performs HTTP Basic Authentication
    """
    if request.authorization.username == config.api_username and request.authorization.password == config.api_password:
        return True
    return False

def authenticate(func):
    """
    Decorator for Auth
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
            
        acct = basic_authentication() 
        
        if acct:
            return func(*args, **kwargs)

        restful.abort(401)
    return wrapper


service = ReportService()


class Resource(restful.Resource):
    """
    Class that expends a Resource and adds HTTP Basic Authentication
    """
    method_decorators = [authenticate]

class PostReportAPI(Resource):
    
    """
    Api for Posting a Report
    Path: /report/
    Method: POST
    Data Format:
        {
            time: <long>,
            difficulty: <int>, 
            title: <string>,
            description: <string>,
            location: {
                 lat: <double>,
                 long: <double>
            }, 
            pic: <string>
        }
    """
    def post(self):
        json_data = request.get_json(force=True) 
        service.insert(json_data)        
    
    
class GetReportAPI(Resource):
    """
    Api for Getting a Report
    Path: /report/<report_id>
    Method: GET
    Data Format:
        {
            id: <id>
            time: <long>,
            difficulty: <int>, 
            title: <string>,
            description: <string>,
            location: {
                 lat: <double>,
                 long: <double>
            }, 
            pic: <?>
        }
    """
    def get(self, report_id):
        return service.get_report(report_id)
    
    
class SearchAPI(Resource):
    """
    """
    def get(self):
        return service.fetch_all()


class SearchByLocationAPI(Resource):
    """
    Api for Search by Location
    """
api.add_resource(GetReportAPI, '/report/<string:report_id>')
api.add_resource(PostReportAPI, '/report/')
api.add_resource(SearchAPI, '/search/')

if __name__ == '__main__':
    app.run(debug=True)