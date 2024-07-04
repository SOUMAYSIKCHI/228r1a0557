fp1 = open("csa.txt","r")
if fp1:
    print("File is opened successfully")
fp1.seek(10,0)
for i in fp1:
    print(i)
    