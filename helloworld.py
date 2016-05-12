
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from datetime import datetime
import os
from paste.deploy import loadapp
from waitress import serve


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    port = int(os.environ.get('PORT', 5000))
    # app = config.make_wsgi_app()
    app = loadapp('config:production.ini', relative_to='.')
    print('{} Starting server on port {}'.format(datetime.now(), port))
    serve(app, host='0.0.0.0', port=port)

    # server = make_server('0.0.0.0', port, app)
    # server.serve_forever()
