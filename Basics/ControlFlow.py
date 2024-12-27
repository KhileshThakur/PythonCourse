#control statement
'''
for , while, pass, break, continue
'''

for i in range(5):
    print(i)
    
count =0
while(count<5):
    print(count)
    count+=1
    
    
'''
match 
'''

value = "siri"
match value:
    case 1:
        print("Hello One")
    case 2:
        print("Hello Two")
    case 3:
        print("Hello Three")
    case _:
        print("Hello Default")
        

'''
nested control
'''

for i in range(5):
    for j in range(i):
        print(f"i={i}, j={j}")
        
#floor division 
print(5/3)
print(5//3)

#Membership operator
'''
in , not in
'''

print('a' in 'apple')
print('x' not in 'apple')

#identity operator
'''
is, is not
'''

print('x' is 'y')
print('x' is not 'y')
print(1+2+
      3+4)

result=1+2+3+\
    4+5
print(result)

'''
Accepts a string from the user prints
each char on a new line
skips space using continue
'''

string_var = input("Enter String: ")
for x in string_var:
    if x==" ":
        continue
    print(x)
    
'''
*
* *
* * *
* * * *
* * * * *
'''

rows = int(input("Enter the no of rows"))
for i in range(1, rows+1):
    print(" * " *i)
    
'''
fibonacii series
'''

n=int(input("Enter the n values : "))
a, b = 0, 1
while a<= n:
    print(a, end=" ")
    a,b = b, a+b
    
#print the odd and even nos from given array
#[1, 2, 3, 4, 5, 6, 7]
list = [1, 2, 3, 4, 5, 6, 7]
odd = []
even = []
for i in list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even no : ", even)
print("Odd ", odd)