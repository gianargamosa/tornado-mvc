from abstract.db import database
import peewee

class CreateUsersTableMigration(AbstactModel):
  def up():
    create_tables([User, Tweet], safe=True)

  def down():
    drop_tables([User, Tweet], safe=True)