# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from testproject.security import groupfinder

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
    
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    
    config = Configurator(settings=settings, root_factory='onlinestore.models.Accesses')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    config.add_route('blog', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('post', '/blog/{id}')
    config.add_route('page', '/page/{nick}')
    config.include('pyramid_sacrud', route_prefix='admin')
    
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (
        ('Tables', [Post,Category,Page,Comment]),)
    config.scan()
    return config.make_wsgi_app()


