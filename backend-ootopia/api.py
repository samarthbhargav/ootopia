# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 14:03:15 2014

@author: Samarth Bhargav
"""

from flask import Flask
from flask.ext import restful
from flask import request

app = Flask(__name__)
api = restful.Api(app)

class PostReportAPI(restful.Resource):

    def post(self):
        json_data = request.get_json(force=True) 
        print json_data
    
    
class GetReportAPI(restful.Resource):
    def get(self, report_id):
        return {'hello': 'world'}
    
    
class SearchAPI(restful.Resource):
    def get(self):
        pass



api.add_resource(GetReportAPI, '/report/<string:report_id>')
api.add_resource(PostReportAPI, '/report/')
api.add_resource(SearchAPI, '/search')

if __name__ == '__main__':
    app.run(debug=True)