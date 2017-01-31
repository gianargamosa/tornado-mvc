from handlers.base_handler import ApplicationHandler, executor
import tornado.ioloop
import tornado.web
from tornado.web import authenticated
import bcrypt
import uuid
import concurrent.futures
from tornado import gen
from models.users_model import Users
from models.posts_model import Posts
from models.relationships_model import Relationships
from channels.posts_channel import PostsChannel

class Users(ApplicationHandler):
  def get(self):
    self.render("settings.html")