#!/usr/bin/env python

import os
import webapp2
import json
import re
import time

from google.appengine.ext import ndb

from model.model import *

from util.json_serializer import JsonSerializer

class LocationStatusController(webapp2.RequestHandler):
            
    def get(self):

        results = []

        # Retrieve attendees
        q = LocationStatus.query().order(-LocationStatus.created_at)

        for location_status in q:
            results.append(location_status)

        self.response.status = 200
        self.outputBody = results
            
        if(self.response.status_int == 200):
            self.response.write(json.dumps(self.outputBody, cls = JsonSerializer, indent=4))


    def post(self):
        
        self.response.status = 422;

        if(self.request.body):

            inputBody = json.loads(self.request.body)
            location_status_update = LocationStatus(**inputBody)

            location_status_update.put()
            self.outputBody = location_status_update
            self.response.status = 201

        if(self.response.status_int == 201): 
            self.response.write(json.dumps(self.outputBody, cls = JsonSerializer, indent=4))
