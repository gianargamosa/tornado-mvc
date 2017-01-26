# coding=utf-8
import yaml
from peewee import *

with open("db/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

MySQL = MySQLDatabase(cfg['mysql']['db'], host=cfg['mysql']['host'], port=3306, user=cfg['mysql']['user'], passwd=cfg['mysql']['passwd'])