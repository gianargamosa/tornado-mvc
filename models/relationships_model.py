# coding:utf-8
from models.base_model import MySQLModel
from peewee import *

class Relationships(MySQLModel):
	id = PrimaryKeyField()
	user_id = IntegerField()
	follower_id = IntegerField()