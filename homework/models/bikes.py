from mongoengine import *

class Bike(Document):
    model = StringField()
    fee = IntField()
    img = URLField()
    year = IntField()