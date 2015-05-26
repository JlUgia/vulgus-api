import json
import datetime
from google.appengine.ext.ndb import GeoPt
from google.appengine.api.search import GeoPoint
from model.model import LocationStatus


class JsonSerializer(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        elif isinstance(obj, GeoPt):
            return {'lat': obj.lat, 'lon': obj.lon}

        elif isinstance(obj, GeoPoint):
            return {'lat': obj.latitude, 'lon': obj.longitude}

        elif isinstance(obj, LocationStatus):
            return obj.to_dict()

        return json.JSONEncoder.default(self, obj)
