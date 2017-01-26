from handlers.base_handler import ApplicationHandler, executor
import tornado.ioloop
import tornado.web
from tornado.web import authenticated
import bcrypt
import concurrent.futures
from tornado import gen
from models.users_model import Users
from models.posts_model import Posts

class Home(ApplicationHandler):
  def get(self):
    # for user in Users.select():
    #   print user.username, user.email
    self.render("home.html", users=Users.select())

class SignUp(ApplicationHandler):
  def get(self):
    self.render("sign_up.html")

  @gen.coroutine
  def post(self):
    user = Users()
    user.username = self.get_argument("username")
    user.email = self.get_argument("email")
    user.password = bcrypt.hashpw(tornado.escape.utf8(self.get_argument("password")), bcrypt.gensalt())
    user.save()
    self.redirect("/sign_up")

class SignIn(ApplicationHandler):
  def get(self):
    self.render("sign_in.html")

  @gen.coroutine
  def post(self):
    user = Users.get(Users.username == self.get_argument("username"))
    if not user:
      print "Username not found"
      self.redirect("/sign_up")

    hashed_password = bcrypt.hashpw(tornado.escape.utf8(self.get_argument("password")), tornado.escape.utf8(user.password))
    if hashed_password == user.password:
      self.set_secure_cookie("user", str(user.username))
      self.redirect('/')
    else:
      self.render("sign_in.html")

class SignOut(ApplicationHandler):
  def get(self):
    self.set_secure_cookie("user", "")
    self.redirect('/sign_in')
