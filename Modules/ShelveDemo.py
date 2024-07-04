import shelve

sh = shelve.open("shelves")

sh['one'] =1
sh['two'] =2
sh['three']=3

sh.close()
