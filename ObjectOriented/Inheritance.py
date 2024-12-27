#Single Inheritance

class parent:
    def greet(self):
        return "Parent Class"
    
class child(parent):
    def greet1(self):
        return "Child Class"
    
obj = child()
print(obj.greet())
print(obj.greet1())



#Multiple Inheritance

class P1:
    def greet1(self):
        return "Parent 1"
class P2:
    def greet2(self):
        return "Parent 2"
class Children(P1, P2):
    pass

obj=Children()
print(obj.greet1())
print(obj.greet2())


#Multilevel Inheritance

class GrandParentClass:
    def greetGP(self):
        return "GrandParentClass"
    
class ParentClass(GrandParentClass):
    def greetP(self):
        return "ParentClass"

class ChildClass(ParentClass):
    def greetC(self):
        return "ChildClass"
    
obj = ChildClass()
print(obj.greetC())
print(obj.greetP())
print(obj.greetGP())


#Heirarchial Inheritance
class MainParent:
    def greetMain(self):
        return "Parent Class"
class Child1(MainParent):
    def greetChild1(self):
        return "Child 1"
class Child2(MainParent):
    def greetChild2(self):
        return "Child 2"
class Child3(MainParent):
    def greetChild3(self):
        return "Child 3"
obj1 = Child1()
print(obj1.greetChild1())
print(obj1.greetMain())
obj2 = Child2()
print(obj2.greetChild2())
print(obj2.greetMain())
obj3 = Child3()
print(obj3.greetChild3())
print(obj3.greetMain())