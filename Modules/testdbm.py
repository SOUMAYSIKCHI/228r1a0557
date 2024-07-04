import dbm
db = dbm.open("dbm1.db",'r')
for k,v in db.items():
    print(k,v)
