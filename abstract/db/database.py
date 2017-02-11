# coding=utf-8
import yaml
from peewee import *

with open("dbconfig.yml", 'r') as ymlfile:
  cfg = yaml.load(ymlfile)

MySQL = MySQLDatabase(cfg['MYSQL']['DB_DATABASE'], host=cfg['MYSQL']['DB_HOST'], port=cfg['MYSQL']['DB_PORT'], user=cfg['MYSQL']['DB_USERNAME'], passwd=cfg['MYSQL']['DB_PASSWORD'])