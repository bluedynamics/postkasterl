# -*- coding: utf-8 -*-
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    settings = config.registry.settings

    # for testing no cache
    max_age = 0 if settings.get('pyramid.reload_templates') else 3600

    config.add_static_view(
        name='/static',
        path='static',
        cache_max_age=max_age
    )

    # routes
    config.add_route('main', pattern='/')

    # pyramid_mailer
    if settings.get('mail.debug', '0') != '0':
        config.include('pyramid_mailer.debug')
    else:
        config.include('pyramid_mailer')

    config.scan('.views')
    return config.make_wsgi_app()
