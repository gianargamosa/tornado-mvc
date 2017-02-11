# coding:utf-8
from models import *

class Users(AbstractModel):
  id = PrimaryKeyField()
  username = CharField(unique=True)
  email = CharField()
  avatar = CharField()
  password = CharField()