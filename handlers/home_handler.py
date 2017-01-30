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

class Home(ApplicationHandler):
  def get(self):
    if not bool(self.current_user):
      self.redirect("/users/sign_in")
    list_of_id = "1, 2, 3"
    posts = Posts.select().where(Posts.user_id << list_of_id.split(',')).order_by(Posts.id.desc())
    print len(posts)
    self.render("home.html", messages=PostsChannel.cache, posts=posts)

class SignUp(ApplicationHandler):
  def get(self):
    if self.current_user:
      self.redirect("/")
    self.render("sign_up.html", errors=None)

  @gen.coroutine
  def post(self):
    errors=[]
    if not self.get_argument("username"):
      errors.append("username is empty")
    if not self.get_argument("email"):
      errors.append("email is empty")
    if not self.get_argument("password"):
      errors.append("password is empty")
    if bool(errors) == True:
      self.render("sign_up.html", errors=errors)
    attributes = [
      {'username': self.get_argument("username"), 'email': self.get_argument("email"), 'password': bcrypt.hashpw(tornado.escape.utf8(self.get_argument("password")), bcrypt.gensalt())},
    ]
    for params in attributes:
      Users.create(**params)
    self.redirect("/users/sign_up")

class SignIn(ApplicationHandler):
  def get(self):
    if self.current_user:
      self.redirect("/users/sign_out")
    self.render("sign_in.html", errors=None)

  @gen.coroutine
  def post(self):
    errors=[]
    if not self.get_argument("username"):
      errors.append("username is empty")
    if not self.get_argument("password"):
      errors.append("password is empty")
    if bool(errors) == True:
      self.render("sign_in.html", errors=errors)
    user = Users.get(Users.username == self.get_argument("username"))
    hashed_password = bcrypt.hashpw(tornado.escape.utf8(self.get_argument("password")), tornado.escape.utf8(user.password))
    if hashed_password == user.password:
      self.set_secure_cookie("user", str(user.username))
      self.redirect('/')
    else:
      self.render("sign_in.html")

class SignOut(ApplicationHandler):
  def get(self):
    self.set_secure_cookie("user", "")
    self.redirect('/users/sign_in')