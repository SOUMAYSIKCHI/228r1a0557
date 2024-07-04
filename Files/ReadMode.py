fp1=open("csa.txt","r")
if fp1:
    print("file s created")
con=fp1.read()
print(con)
print(fp1.tell())
