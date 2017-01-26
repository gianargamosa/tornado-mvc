
import tornado.web
import torndb
import concurrent.futures
from models.users_model import Users
from models.posts_model import Posts

executor = concurrent.futures.ThreadPoolExecutor(2)

class ApplicationHandler(tornado.web.RequestHandler):
  
  def get_current_user(self):
    username = self.get_secure_cookie("user")
    user = None
    if username:
      user = Users.get(Users.username == username)
    return user
      
  def any_user_exists(self):
    return bool(Users.get().limit(1))

  def get_object_or_404(model, *expressions):
    try:
      return model.get(*expressions)
    except model.DoesNotExist:
      abort(404)