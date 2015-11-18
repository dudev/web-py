# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from sqlalchemy import engine_from_config



from .models import (
    DBSession,
    Post,
    Category,
    Page,
    Comment,
    Base
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('blog', '/')
    config.add_route('post', '/blog/{id}')
    config.add_route('page', '/page/{nick}')
    config.include('pyramid_sacrud', route_prefix='admin')
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (
        ('Tables', [Post,Category,Page,Comment]),)
    config.scan()
    return config.make_wsgi_app()


