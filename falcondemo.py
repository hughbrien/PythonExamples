# things.py

# Let's get this party started!
import falcon
import instana
from instana.wsgi import iWSGIMiddleware

import opentracing as ot



# -*- coding: utf-8 -*-
import re
import sys

instana.service_name = "Falcon_Service"

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.


class ThingsResource(object):

    def on_get(self, req, resp):

        with ot.tracer.start_active_span('universe') as escope:
            escope.span.set_tag('http.method', 'GET')
            escope.span.set_tag('http.url', '/things')
            escope.span.set_tag('span.kind', 'entry')
            """Handles GET requests"""
            resp.status = falcon.HTTP_200  # This is the default status
            resp.body = ('\nTwo things awe me most, the starry sky '
                         'above me and the moral law within me.\n'
                         '\n'
                         '    ~ Immanuel Kant\n\n')


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
