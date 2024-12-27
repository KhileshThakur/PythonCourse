'''
class: collection of functions and attribute
object : instance of a class
class classname
    name , add, sal
    def __init__(self, name, age):
        a, B, C
'''


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #method
    def greet(self):
        return f"my name is {self.name} and age is {self.age}"
person1=person("Alice", 34)
person2=person("Bob", 43)
print(person1.greet())
print(person2.greet())



#__str__ Method
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"person {self.name} and age is {self.age}"
    
ob=A("Alice", 45)
print(ob)
# print(str(ob))


# 