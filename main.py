#!/usr/bin/env python

# Google's AppEngine modules:
import webapp2
from webapp2 import Route
from webapp2_extras import routes
from webapp2_extras.routes import DomainRoute

# Controllers and handlers
from controller.location_status import *
from controller.location_status_search_api import *

# Requested URLs that are not listed here,
# will return 404

ROUTES = [
    DomainRoute('<:(localhost|vulgusapp\.appspot\.com)>', [

        routes.PathPrefixRoute(r'/api/1', [

            # Location endpoints
            Route(r'/location_status', handler=LocationStatusController),
            Route(r'/location_status_search',
                  handler=LocationStatusSearchController)

        ])
    ])
]

app = webapp2.WSGIApplication(ROUTES, debug=False)
