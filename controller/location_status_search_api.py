#!/usr/bin/env python

import webapp2
import json

import logging

from google.appengine.api import search

from util.json_serializer import JsonSerializer

FIFTY_KM_METERS = 50000


class LocationStatusSearchController(webapp2.RequestHandler):

    def post(self):

        logging.info(self.request.body)
        inputBody = json.loads(self.request.body)

        if inputBody is None or 'current_location' not in inputBody:
            self.response.status = 422
        else:

            locations = []

            coords = inputBody['current_location'].split(",", 1)
            lat = float(coords[0])
            lon = float(coords[1])

            index = search.Index(name='locationIndex')
            result = index.search('distance(location, geopoint(%f, %f)) < %d' %
                                  (lat, lon, FIFTY_KM_METERS))

            for doc in result.results:
                locations.append(doc.fields[0].value)

            self.response.status = 200

        if(self.response.status_int == 200):
            self.response.write(json.dumps(locations, cls=JsonSerializer))

    def put(self):

        self.response.status = 422

        if(self.request.body):

            inputBody = json.loads(self.request.body)

            coords = inputBody['location'].split(",", 1)
            lat = float(coords[0])
            lon = float(coords[1])

            status_document = search.Document(doc_id=inputBody['instance_id'],
                                              fields=[search.GeoField(
                                                  name='location',
                                                  value=search.GeoPoint(
                                                      lat, lon
                                                  ))])

            try:
                index = search.Index(name="locationIndex")
                index.put(status_document)

                self.response.status = 201

            except search.Error:
                logging.exception('Put failed')
