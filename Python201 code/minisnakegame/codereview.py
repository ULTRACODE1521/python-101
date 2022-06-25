class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p2 = Person("Jonathan", 24)
 
print(p1.name)
print(p1.age)
p1.myfunc()

print(p2.name)
print(p2.age)
p2.myfunc()