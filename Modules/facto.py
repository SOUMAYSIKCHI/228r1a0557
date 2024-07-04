import marshal
src = '''
def factoo(n):
    if(n==0):
        return 1
    return n*(factoo(n-1))

print(factoo(5))
'''
code = compile(src,"src","exec")
fp = open("facto.txt", "wb")
marshal.dump(code,fp)
fp.close()