from mongoengine import *

con1 = connect(alias='db1', db='mycustomers')
con2 = connect(alias='db2', db='db')
con3 = connect(alias='db3', db='mystudents')

dbs=con1.list_database_names()
print ('mycustomers dbs:')
for db in dbs:
    print (db)

dbs=con2.list_database_names()
print ('db dbs:')
for db in dbs:
    print (db)

dbs=con3.list_database_names()
print ('mystudents dbs:')
for db in dbs:
    print (db)


print ("--------------------------------------------------------------------------------")

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


for altstu in altstudent.objects.filter(name='Mohan Lal'):
    print(altstu.studentid)
    print(altstu.name)
    print(altstu.age)
    print(altstu.percent)
    print(altstu.email)
    print(altstu.tid)
    print(altstu.subjects)
    print(altstu.score)