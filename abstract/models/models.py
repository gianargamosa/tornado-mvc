from peewee import *
from abstract.db.database import MySQL

class AbstractModel(Model):
  class Meta:
    database = MySQL