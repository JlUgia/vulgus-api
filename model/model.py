#!/usr/bin/env python

from neoproperty.properties import *

from google.appengine.ext import ndb

# These classes define the data objects
# that you will be able to store in
# AppEngine's data store.


class LocationStatus(ndb.Model):
    location = NeoGeoPtProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)

    def to_dict(self):
        return {'id': str(self.key.id()), 'location': self.location,
                'created_at': self.created_at}

    def __hash__(self):
        return self.key().id()

    def __eq__(self, other):
        return self.key().id() == other.key().id()
