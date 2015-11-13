from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    String,
    DateTime,
    func
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    post = relationship("Post", backref="category")


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    email = Column(String)
    author = Column(String, nullable=False)
    create_time = Column(DateTime, default=func.now(), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    nick = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    public_time = Column(DateTime, default=func.now(), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    comment = relationship("Comment", backref="post")
    category = relationship("Category")