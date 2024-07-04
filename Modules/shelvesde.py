import shelve

with shelve.open("shelves2ndfile") as sh:
    sh['one'] =1
    sh['two'] =2
    sh['three']=3

sh.close()
