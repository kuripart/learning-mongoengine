from mongoengine import *

connect(alias='db1', db='mycustomers')
connect(alias='db2', db='db')

# working with multiple connections: https://stackoverflow.com/a/56434241 
class student(DynamicDocument):
    meta = {"db_alias": "db2"}
    name=StringField()

s1=student()
setattr(s1,'age',20)
s1.name='Lara'
s1.save()


class store(Document):
    meta = {"db_alias": "db1"}
    storeid = StringField(required=True)
    name = StringField(max_length=50)
    year = IntField()
    def _init__(self, id, name, year):
       self.storeid=id,
       self.name=name
       self.year=year

# s1=store('a001', 'bora', 2009) --> TypeError: Instantiating a document with positional arguments is not supported. Please use `field_name=value` keyword arguments
s1=store(storeid='a001', name='bora', year=2009)
s1.save()