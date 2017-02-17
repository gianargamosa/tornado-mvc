from main_activity import *
from abstract.models.users_model import *

class Main(GradleActivity):
  def get(self):
    users = Users.select()
    for user in users:
      print user.username
    self.render("main.html", title="Gradle Todo Application")