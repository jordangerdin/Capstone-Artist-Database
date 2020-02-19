from peewee import *
from sql_database.config import db_path

db = SqliteDatabase(db_path)

class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    name = CharField()
    email = CharField()

    #def __str__(self):
    #   return f'Name: {self.name}, Email: {self.email}'

class Artwork(BaseModel):
    artist = ForeignKeyField(Artist)
    artwork = CharField()
    price = DecimalField()
    available = BooleanField()

    #def __str__(self):
    #    return f'{self.artwork} by {self.artist}, ${self.price}, available: {self.available}'

db.connect()
db.create_tables([Artist, Artwork])