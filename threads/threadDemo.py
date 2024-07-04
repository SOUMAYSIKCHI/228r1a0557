import threading

def cal(n):
    print("Thread",10)

def sqr(n):
    print("square",n*n)

def cube(n):
    print("cube =",n*n*n)

# t1 = threading.Thread(target=cal,args=(10,))
t2 = threading.Thread(target=sqr,args=(10,))
t3 = threading.Thread(target=cube,args=(10,))

t3.start()
t2.start()
t3.join()
t2.join()
