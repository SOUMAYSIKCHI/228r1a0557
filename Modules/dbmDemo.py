import dbm

db = dbm.open("dbm1.db",'n') #r ,c
db['one']='1'
db['two']='2'

#with dbm.open("dbm.db") as db:
