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
from flask_cors import CORS
from entity import Report
import flask
import datetime
 
app = Flask(__name__, static_folder='static', static_url_path='')
#app = Flask(__name__)
cors = CORS(app)

@app.after_request
def add_cors(resp):
    """ Ensure all responses have the CORS headers. This ensures any failures are also accessible
        by the client. """
    resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin','*')
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get( 
        'Access-Control-Request-Headers', 'Authorization' )
    # set low for debugging
    if app.debug:
        resp.headers['Access-Control-Max-Age'] = '1'
    return resp
    
api = restful.Api(app)


class Hello(restful.Resource):
    def get(self):
        return { "Hello" : "World"}



def basic_authentication():
    """
    Performs HTTP Basic Authentication
    """
    if request.authorization is not None and request.authorization.username == config.api_username and request.authorization.password == config.api_password:
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


class PostReportAPI(restful.Resource):
    
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
        json_data["status"] = "New"
        print json_data
        service.insert(json_data)
        return {"message":"Report successfully added"}
    

class GetReportAPI(restful.Resource):
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
    

class SearchAPI(restful.Resource):
    """
    """
    def get(self):
        return service.fetch_all()


class SearchByLocationAPI(restful.Resource):
    """
    Api for Search by Location
    """
    def get(self, location):
        return service.get_reports_by_location(location)

    
class UpdateReportStatusAPI(restful.Resource):
    
    def put(self, Id, new_status):
        service.update_status(Id, new_status)


class GetImageAPI(restful.Resource):
    
    def get(self, report_id):
        return app.send_static_file(report_id + ".jpg")
        

class GetMapPage(restful.Resource):
    
    def get(self):        
        return app.send_static_file("page.html")
        

@app.route('/render/<report_id>')
def render(report_id):
    report = service.get_report(report_id)
    report["time"] = datetime.datetime.fromtimestamp(report["time"] / 1000).strftime('%d-%m-%Y %H:%M:%S')
    return flask.render_template('render_report.html', data=(report))

    
api.add_resource(GetReportAPI, '/report/<string:report_id>')
api.add_resource(GetImageAPI, '/report/<string:report_id>/image/')
api.add_resource(PostReportAPI, '/report')
api.add_resource(SearchAPI, '/search')
api.add_resource(SearchByLocationAPI, '/search/<string:location>')
api.add_resource(Hello, '/hello')
api.add_resource(UpdateReportStatusAPI, '/report/<string:Id>/<string:new_status>')
api.add_resource(GetMapPage, '/page.html')
#api.add_resource(RenderReport, '/render/<string:report_id>.html')


if __name__ == '__main__':
    app.run(debug=True)