# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    String,
    DateTime,
    Unicode,
    UnicodeText,
    func
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from pyramid.security import (
    Allow,
    Everyone
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    post = relationship("Post")


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(UnicodeText, nullable=False)
    email = Column(Unicode(255))
    author = Column(Unicode(255), nullable=False)
    create_time = Column(DateTime, default=func.now(), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    nick = Column(Unicode(255), unique=True, nullable=False)
    content = Column(UnicodeText, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    content = Column(UnicodeText, nullable=False)
    public_time = Column(DateTime, default=func.now(), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    comment = relationship("Comment", backref="post")
    category = relationship("Category")

class Accesses(object):
    __acl__ = [ (Allow, 'group:editors', ('pyramid_sacrud_home', 'pyramid_sacrud_create', 'pyramid_sacrud_update', 'pyramid_sacrud_delete', 'pyramid_sacrud_list')),
                (Allow, 'Everyone', 'view') ]
    def __init__(self, request):
        pass
