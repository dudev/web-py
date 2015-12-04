# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import (
    view_config,
    forbidden_view_config)

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Post,
    Category,
    Page,
    Comment
    )

from pyramid.httpexceptions import HTTPFound

from pyramid.security import (
    remember,
    forget)

from .security import USERS

@view_config(route_name='post', request_method='GET', renderer='/root/web-py/testproject/templates/post.jinja2')
def post_view(request):
    post_id = request.matchdict['id']
    post = DBSession.query(Post).filter_by(id=post_id).first()
    comments = DBSession.query(Comment).filter_by(post_id=post_id).all()
    categories = DBSession.query(Category).all()
    if not post:
        return Response('Not found')
    return {'post' : post, 'comments' : comments, 'categories' : categories, 'report': 0}

@view_config(route_name='post', request_method='POST', renderer='/root/web-py/testproject/templates/post.jinja2')
def post_comment(request):
    post_id = request.matchdict['id']
    post = DBSession.query(Post).filter_by(id=post_id).first()
    categories = DBSession.query(Category).all()
    try:
        author = request.POST['author']
        email = request.POST['email']
        content = request.POST['content']
        if not (author and email and content):
            return {'post' : post, 'categories' : categories, 'report': 2}
        comment = Comment(
            content = content,
            email = email,
            author = author,
            post_id = post_id
        )
        DBSession.add(comment)
    except Exception as ex:
        print ex
        return {'post' : post, 'categories' : categories, 'report': 3}
    
    return {'post' : post, 'categories' : categories, 'report': 1}


@view_config(route_name='blog', renderer='/root/web-py/testproject/templates/blog.jinja2')
def blog_view(request):
    categories = DBSession.query(Category)
    category = None
    if 'cat' in request.GET:
        category_id = request.GET['cat']
        category = categories.filter_by(id=category_id).first()
    if category:
        posts = category.post
    else:
        posts = DBSession.query(Post).all()
    return {'posts': posts,
            'categories': categories}


@view_config(route_name='page', renderer='/root/web-py/testproject/templates/page.jinja2')
def page_view(request):
    page_nick = request.matchdict['nick']
    page = DBSession.query(Page).filter_by(nick=page_nick).first()
    categories = DBSession.query(Category).all()
    if not page:
        return Response('Not found')
    return {'page' : page, 'categories' : categories}

@view_config(route_name='login', request_method='GET', renderer='/root/web-py/testproject/templates/login.jinja2')
@forbidden_view_config(renderer='/root/web-py/testproject/templates/login.jinja2')
def login(request):
    categories = DBSession.query(Category).all()
    return {'login': '', 'categories' : categories}

@view_config(route_name='login', request_method='POST', renderer='/root/web-py/testproject/templates/login.jinja2')
def login(request):
    login = ''
    password = ''
    if (login and password):
        login = request.params['login']
        password = request.params['password']
        if USERS.get(login) == password:
            headers = remember(request, login)
            return HTTPFound(location = '/admin',
                             headers = headers)
    categories = DBSession.query(Category).all()
    return {'message': 'Неверный логин или пароль', 'login': login, 'categories' : categories }

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = '/',
                     headers = headers)
