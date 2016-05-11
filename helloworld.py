#!/usr/bin/env python

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from datetime import datetime
import os


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    port = int(os.environ['PORT'])
    server = make_server('ottpau-hello.herokuapp.com', port, app)
    print('{} Starting server on port {}'.format(datetime.now(), port))
    server.serve_forever()
