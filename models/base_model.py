# coding=utf-8
from peewee import *
from db.database import MySQL

class MySQLModel(Model):
  class Meta:
    database = MySQL