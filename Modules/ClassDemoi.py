class myclass:
    x = 10

class myclass2:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

obj=myclass()
p1 = myclass2("hello", "hi")
print(p1.name)
print(obj.x)
