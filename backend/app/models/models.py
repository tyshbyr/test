from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from passlib.context import CryptContext

from app.models.base import Base

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="user")
    subscriptions = relationship("Subscription", back_populates="user")
    post_reads = relationship("PostRead", back_populates="user")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = pwd_context.hash(password)


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="blogs")
    posts = relationship("Post", back_populates="blog")
    subscriptions = relationship("Subscription", back_populates="blog")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    title = Column(String)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    blog = relationship("Blog", back_populates="posts")
    post_reads = relationship("PostRead", back_populates="post")


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    blog_id = Column(Integer, ForeignKey('blogs.id'))

    user = relationship("User", back_populates="subscriptions")
    blog = relationship("Blog", back_populates="subscriptions")


class PostRead(Base):
    __tablename__ = 'post_reads'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    user = relationship("User", back_populates="post_reads")
    post = relationship("Post", back_populates="post_reads")
