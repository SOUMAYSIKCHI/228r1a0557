import shelve

sh = shelve.open("shelves")
print(list(sh.keys()))
print(list(sh.values()))
print(list(sh.items()))
