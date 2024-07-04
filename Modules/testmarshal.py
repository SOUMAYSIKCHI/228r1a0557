import marshal
fp =open("facto.txt", "rb")
data = marshal.load(fp)
exec(data)