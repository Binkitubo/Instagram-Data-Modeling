import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(10), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    filetype = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Likes(Base):
    __tablename__ = 'likes'
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comments'
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String(250))

class Followers(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e