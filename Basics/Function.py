#BuiltIn Function
'''
print(), len(), type()
'''



#User Defined Functions
'''
using def
'''
def greet(name):
    return f"Hello, {name}"

print(greet("Khilesh"))

#default arguments
def greet_default(name="Khilesh"):
    return f"Hello, {name}"

print(greet_default())
print(greet_default("Avir"))

#variable length argument
'''
*args:non keyword argument
**kwargs: keyword argument
'''

def print_args(*args):
    print(args)
def print_kwargs(**kwargs):
    print(kwargs)
    
print_args(1, 2, 3, 4)
print_kwargs(a=1, b=2)


#Anonymous function
'''
Lambda function
'''

square=lambda x:x**2
print(square(5))

add=lambda a,b:a+b
print(add(2, 4))


#Recursive function

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

#filter, map, reduce, enumerate
number=[1, 2, 3, 4, 5, 6]
even=filter(lambda x:x%2==0, number)
print(list(even))

number=[1, 2, 3, 4, 5, 6, 7]
square_nos=map(lambda x:x**2, number)
print(list(square_nos))

from functools import reduce
nos = [1, 2, 3, 4, 5, 6, 7, 8]
product = reduce(lambda x,y:x*y, nos)
print(product)

items=['a', 'b', 'c', 'd', 'e']
for idx, val in enumerate(items):
    print(idx, val)

#Nested functions for dynamic operations

def calculator(operation):
    def add(a, b): return a+b
    def sub(a, b): return a-b
    def mul(a, b): return a*b
    def div(a, b): return a/b
    
    operations={
        "addition": add, 
        "subtract": sub,
        "multiply": mul,
        "division": div
    }
    
    return operations.get(operation, lambda a, b:"invalid operation")

add_fun = calculator("addition")
print(add_fun(5, 6))
mul_fun = calculator("multiply")
print(mul_fun(6, 8))

'''
Accept List of Integer from user
-use filter and lambda function to extract all nums
-divisible by 3 or 5
'''

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
filter_nos = filter(lambda x:x%3==0 or x%5==0, nos)
print("result : ", list(filter_nos))

'''
Accept a nested list : [[1, 2], [3, 4], [5, 6]]
use map to flatten the list in to a single list [1, 2, 3, 4, 5, 6]
'''


'''
Accept the string from user, 
use map and reduce to count the frequency of each character
'''


'''
Accepts a list of integers from the user user reduce to find the maximum number
'''


from functools import reduce 
numbers = list(map(int, input("Enter Nos : ").split()))
max_no = reduce(lambda x,y: x if x>y else y, numbers)
print(max_no)

