# coding:utf-8
from models.base_model import MySQLModel
from peewee import *

class Posts(MySQLModel):
  id = PrimaryKeyField()
  user_id = CharField()
  body = TextField()
  stamp = DateTimeField()