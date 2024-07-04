'''
open()
read()
readline()
write()
writeline()
close()
fseek()
tell()

'''
fp=open("csa.txt","w")
if fp:
    print("file is opened successfully")
fp.writelines("hi students welcome to cmrec \n")


fp.close()