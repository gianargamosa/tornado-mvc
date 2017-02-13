#coding:utf-8
import tornado.ioloop
import tornado.options
from tornado.options import define, options
import tornado.web
import os
import yaml
import tornado.options
import concurrent.futures
from routes import *

with open("env.yml", 'r') as ymlfile:
  cfg = yaml.load(ymlfile)

settings = dict(
  template_path=os.path.join(os.path.dirname(__file__), cfg['ENV']['APP_TEMPLATE']),
  static_path=os.path.join(os.path.dirname(__file__), cfg['ENV']['APP_ASSETS']),
  cookie_secret=cfg['ENV']['APP_KEY'],
  xsrf_cookies=cfg['ENV']['APP_XSRF'],
  login_url="/sign_in",
  debug=cfg['ENV']['APP_DEBUG'],
)

def make_app():
  return tornado.web.Application(route, **settings)

if __name__ == "__main__":
  app = make_app()
  app.listen(8500)
  tornado.options.parse_command_line()
  print '=> Booting Gradle'
  print '=> Application started in '+ cfg['ENV']['APP_ENV'] +' on '+ cfg['ENV']['APP_URL'] +':%s/' % 8000
  print '=> Run `python server.py -h` for more startup options'
  tornado.ioloop.IOLoop.current().start()