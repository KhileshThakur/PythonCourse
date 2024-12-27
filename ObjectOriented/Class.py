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


# main Method

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def main():
    print("Choose Option: ")
    print("1. Addition")
    print("2. Subtract")
    choice = input("Enter Choice : ")
    n1 = int(input("Enter first Number : "))
    n2 = int(input("Enter Second Number : "))
    
    if choice == '1':
        print(f"result : {add(n1, n2)}")
    elif choice == '2':
        print(f"result: {sub(n1, n2)}")
    else:
        print("Invalid Number ")
if __name__=="__main__":
    main()