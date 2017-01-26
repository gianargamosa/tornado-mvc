#coding:utf-8
from handlers.base_handler import ApplicationHandler, executor
import tornado.web
from tornado import gen
import bcrypt
import concurrent.futures

class SignUpHandler(ApplicationHandler):
  def get(self):
    self.render("users/sign_up.html")

  @gen.coroutine
  def post(self):
    if self.any_user_exists():
      self.clear()
      self.set_status(400)
      self.render('../public/404.html', errors=tornado.web.HTTPError(400))
      raise tornado.web.HTTPError(400, "author already created")
    hashed_password = yield executor.submit(
      bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
      bcrypt.gensalt())
    author_id = self.db.execute(
      "INSERT INTO users (username, email, name, hashed_password) VALUES (%s, %s, %s, %s)",
        self.get_argument("username"), self.get_argument("email"), self.get_argument("name"), hashed_password)
    self.set_secure_cookie("blogdemo_user", str(author_id))
    self.redirect(self.get_argument("next", "/"))

class SignInHandler(ApplicationHandler):
  def get(self):
    if not self.any_user_exists():
        self.redirect("/auth/sign_up")
    else:
        self.render("users/sign_in.html", error=None)

  @gen.coroutine
  def post(self):
    author = self.db.get("SELECT * FROM users WHERE email = %s", self.get_argument("email"))
    if not author:
        self.render("users/sign_in.html", error="email not found")
        return
    hashed_password = yield executor.submit(
        bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        tornado.escape.utf8(author.hashed_password))
    if hashed_password == author.hashed_password:
        self.set_secure_cookie("blogdemo_user", str(author.id))
        self.redirect(self.get_argument("next", "/"))
    else:
        self.render("users/sign_in.html", error="incorrect password")
