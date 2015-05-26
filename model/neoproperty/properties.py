#!/usr/bin/env python

from google.appengine.ext import ndb

GeoPt = ndb.GeoPt


class NeoGeoPtProperty(ndb.GeoPtProperty):

    def _validate(self, value):
        if not isinstance(value, GeoPt) and not isinstance(value, basestring):
            raise ValueError('Expected GeoPt or basestring, got %r' % (value,))

        return value

    def _set_value(self, entity, value):

        if isinstance(value, GeoPt):
            lat = value.lat
            lon = value.lon

        elif isinstance(value, basestring):
            coords = value.split(",", 1)
            lat = coords[0]
            lon = coords[1]
            value = GeoPt(lat, lon)

        entity._values[self._name] = value
