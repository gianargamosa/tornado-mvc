# coding:utf-8
from models.base_model import MySQLModel
from peewee import *

class Users(MySQLModel):
  id = PrimaryKeyField()
  username = CharField(unique=True)
  email = CharField()
  avatar = CharField()
  password = CharField()