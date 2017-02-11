from main_activity import *
from abstract.models.users_model import *

class Main(MainActivity):
  def get(self):
    users = Users.select()
    for user in users:
      print user.username
    self.render('main.html')