a = int(input("Enter a value"))
b = int(input("Enter b value"))

try:
    c=a/b
    print("VALUE OF C = ",c)
    x =[1,2,3]
    print(x[5])
except NameError:
    print("B value is not crct")
except ZeroDivisionError:
    print("Arithmetic exception")
except IndexError:
    print("Index error")

