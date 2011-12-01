"""
"""
from pyramid.config import Configurator
# from pyramid.httpexceptions import (
#     HTTPClientError,
#     HTTPMethodNotAllowed)
# from pyramid.view import view_config
# from pyramid.response import Response


def app_factory(global_settings, **local_settings):
    """
    """
    config = Configurator(settings=local_settings)
    config.add_route('index', '/')
    config.scan()
    return config.make_wsgi_app()
