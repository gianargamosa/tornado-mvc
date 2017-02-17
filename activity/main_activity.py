import tornado.web
import torndb
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(2)

class GradleActivity(tornado.web.RequestHandler):
  def __init__(self, application, request, **kwargs):
    super(GradleActivity, self).__init__(application, request)

  def write_error(self, status_code, **kwargs):
    if status_code == 404:
      self.render('errors/404.html',page=None)
    else:
      self.render('errors/unknown.html',page=None)