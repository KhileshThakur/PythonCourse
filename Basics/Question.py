'''
1. Write a program 


'''
from functools import reduce
employees=[
    {"name":"siri", "salary":55000},
    {"name":"sirish", "salary":40000},
    {"name": "sirinjan", "salary":60000},
    {"name": "sirsha", "salary":30000}
]
high_sal=filter (lambda emp:emp["salary"]>50000, employees)
name=map(lambda emp:emp['name'], high_sal)
res=reduce(lambda x,y:f"{x}, {y}", name)
print(res)

'''
prime No. between range
'''
# def prime_nos(n1, n2):
#     primes = []
#     for num in range(n1, n2+1):
#         if num>1:
#             for i in range(2, num):
#                 if num%i==0:
#                     break
#             else:
#                 primes.append(num)
#     return primes

# n1=int(input("Enter n1 value : "))
# n2=int(input("Enter the n2 value: "))
# res=prime_nos(n1, n2)
# print(res)


'''
calculate the sum of digits 
identify if the sum of digits is itself a prime
store the results in a dictionary with prime number

'''

def prime_nos(n1, n2):
    primes = []
    sum = 0
    for num in range(n1, n2+1):
        if num>1:
            for i in range(2, num):
                if num%i==0:
                    break
            else:
                primes.append(num)
                sum += num
    for i in range(1, sum+1):
        if sum%i==0 and sum>1:
            break
        else:
            print("Sum is prime")
    return primes, sum

n1=int(input("Enter n1 value : "))
n2=int(input("Enter the n2 value: "))
res=prime_nos(n1, n2)
print(res)


'''
7. Write a function that takes a list of elements
- group the elements by frequency
1/p:[1,1,1,2,3,3,4,5,6,6,6]
o/p: [1,3,6]
- create the unque pairs from list
i/p: [1,2,3] 12=[3,4,5]
o/p:[(1,3), (1,4), (1,5).....]
- Find the first non repeated element
i/p: [4,5,1,2,1,4,3]
op:5
- merge two sorted lists without duplicates
'''