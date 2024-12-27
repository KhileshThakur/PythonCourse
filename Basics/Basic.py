#Assignment Operator
x = 14
y = 2.3

#Control Statement
if x>5:
    print("x is +ve no")

#Expression Statement
res = 2+4
print(res)

#Comment
'''
Multiple line Comment
'''

#Command Line argument
#pass the inputs to python script 
#Executed from command line 
#module: sys

import sys
print("Name: ", sys.argv[0])
if len(sys.argv)>1:
    print("arguments : ", sys.argv[1:])
else:
    print("No arguments provided")
    
#Getting user input
# name = input("Enter Your Name : ")
# print(f"Hello, {name}")
# age = int(input("Enter Your Age : "))
# print(f"You are {age} years old")

#variables
x = 10
y = "slice"
pi = 3.134

a=b=c=43
print(a, b, c)
x, y, z=1, 2.3, "Hello"
print(x, y, z)

#implicit type conversion(Type Coercion)

num_str = "123"
print(num_str)
print(res, type(res))

list1 = [1, 2, 3]
tuple1 = tuple(list1)
print(tuple1, type(tuple1))


#Data Type
'''
Integer(int)
Float(float)
Complex(complex)
'''

z=3+4j
print(z, type(z))

#Sequence Types:

'''
1. String(str)
2. List(list)--> Mutable
3. Typle(tuple)--> Immutable
4. Range(range)--> Sequence of numbers
'''

mylist = [1, 2, 4, '455']
print(mylist, type(mylist))

range_v = range(5)
print(list(range_v), type(range_v))

#Set Types
'''
Set(set) --> unordered
Dictionary(dict) --> unordered collection of key : value
'''

#boolean
'''
Boolean(bool)
'''