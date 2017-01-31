#coding:utf-8
import tornado.ioloop
import tornado.options
from tornado.options import define, options
import tornado.web
import os
import tornado.options
import concurrent.futures
from handlers import *
from channels import *

settings = dict(
  template_path=os.path.join(os.path.dirname(__file__), "views"),
  static_path=os.path.join(os.path.dirname(__file__), "assets"),
  cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
  xsrf_cookies=True,
  login_url="/sign_in",
  debug=True,
)

def make_app():
  return tornado.web.Application([
    (r"/", Home),
    (r"/settings", Users),
    (r"/chatsocket", PostsChannel),
    (r"/users/sign_up", SignUp),
    (r"/users/sign_out", SignOut),
    (r"/users/sign_in", SignIn),
  ], **settings)

if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.options.parse_command_line()
  print '=> Booting Acorn'
  print '=> Fence 0.0.1 application starting in development on http://127.0.0.1:%s/' % 8000
  print '=> Run `python server.py -h` for more startup options'
  tornado.ioloop.IOLoop.current().start()
