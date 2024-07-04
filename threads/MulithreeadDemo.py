import threading
import time

def square(num):
    for n in num:
        time.sleep(0.5)
        print("square = ",n*n)

def cube(num):
    for n in num:
        time.sleep(0.7)
        print("cube = ",n*n*n)

arr=[1,2,3,4]

t1 = threading.Thread(target=square,args=(arr,))
t2 = threading.Thread(target=cube,args=(arr,))
t1.start()
t2.start()
t2.join()