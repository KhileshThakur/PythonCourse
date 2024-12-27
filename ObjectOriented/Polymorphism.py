#Method Overloading
'''
Python Do not support method overloading because of its dynamic nature
variables are decided at runtime


but we can achieve it by default arguments
'''

class cal:
    def add(self, a, b=0, c=0):
        return a+b+c
calc = cal()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(2, 3, 4))


#Method Overriding

class P:
    def greet(self):
        return "Hello Parent"
class Ch(P):
    def greet(self): #overiding the method
        return "Hello Child"
    
ob = Ch()
print(ob.greet())