from mongoengine import *

connect(alias='db1', db='mycustomers')
connect(alias='db2', db='db')
connect(alias='db3', db='mystudents')

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


class student(Document):
    meta = {"db_alias": "db3"}
    studentid = StringField(required=True)
    name = StringField()
    age = IntField(min_value=6, max_value=50)
    percent = DecimalField(precision=2)
    email = EmailField()
s1=student()
s1.studentid='001'
s1.name='Mohan Lal'
s1.age=40
s1.percent=75
s1.email='mohanlal@gmail.com'
s1.save()

class teacher(Document):
    meta = {"db_alias": "db3"}
    tid=StringField(required=True)
    name=StringField()

class altstudent(Document):
    meta = {"db_alias": "db3"}
    studentid = StringField(required=True)
    name = StringField()
    age = IntField(min_value=6, max_value=50)
    percent = DecimalField(precision=2)
    email = EmailField()
    tid=ListField(ReferenceField(teacher))
    subjects = ListField(StringField())
    score = DictField()


t1=teacher()
t1.tid='T1'
t1.name='Murthy'
t1.save()

t2=teacher()
t2.tid='T2'
t2.name='Saxena'
t2.save()

s1=altstudent()
s1.studentid='001'
s1.name='Mohan Lal'
s1.age=40
s1.percent=75
s1.email='mohanlal@gmail.com'
s1.subjects=['phy', 'che', 'maths']
s1.score['phy']=60
s1.score['che']=70
s1.score['maths']=80
s1.tid=[t1,t2]
s1.save()