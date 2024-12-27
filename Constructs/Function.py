'''
Function is block of code that performs a specific task.

def keyword for defining 

'''

#Function with default parameter
def greet(name="John"):
    return f"Hello, {name}"

print(greet())
print(greet("Khilesh"))

#Function with arbitary argument
def print_items(*items):
    for item in items:
        print(item)
print_items("Apple", "Banana", "Cherry", "Dragonfruit")

#Function with keyword argument
def person(name, age):
    print(f"{name} is {age} years old!")

person(age=20, name="Khilesh")

#lambda (anonymous) function
add = lambda x, y: x+y
print(add(3, 4))


#Mathematical Function
print(abs(-10))
print(pow(2, 3))
print(round(3.2345563, 3))

print(id(42))
# print(dir([]))
# help(print())


# open()----->close() automatically
# with open()

# with open("file.txt", "r") as file:
#     print(file.read())
    

#eval 
print(eval("3-(8-5)"))
exec("x=5; print(x)")
print(list(zip([1,2],['a', 'b'])))


#passing a function as an argument
def squaref(x):
    return x**2

def cubef(x):
    return x**3

def apply_function(func, val):
    return func(val)

print(apply_function(squaref, 4))
print(apply_function(cubef, 4))


#Returning a function from another function 
def multiply(fact):
    def mult(value):
        return value*fact
    return mult
double=multiply(2)
print(double(5))


#function as both argument and return 
def transform(func):
    def inner(value):
        return func(value)*2
    return inner 

def add_one(x):
    return x+1

add_double = transform(add_one)
print(add_double(5))


#passing and returning lambda function

def pass_lamda(func, value):
    return func(value)*2
res = pass_lamda(lambda x:x+3, 4)
print(res)

#lamda with default argument
power=lambda x,y=2:x**y
print(power(3))
print(power(3, 3))

words = ['apple', 'banana', 'kiwi']
sort_ele=sorted(words, key=lambda word:len(word))
print(sort_ele)


#inline conditional in lambda
is_even=lambda x:"even" if x%2==0 else "odd"
print(is_even(4))
print(is_even(3))


#nested lambda function 

nested=lambda x:lambda y:x+y
add_five=nested(5)
print(add_five(10))



#QUESTIONS

'''
Write a function operate_list(operation, nums)
takes a function (operation) and a list of nos as arguments 
applies the function to all elements in the list and returns a new list.
'''

def double(x):
    return x*2

def operate_list(func, nums):
    return [func(num) for num in nums]
        
print(operate_list(double, [1, 2, 3, 4]))

'''

'''