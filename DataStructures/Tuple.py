'''
Tuple :
    - Immutable
    - Fixed data operation
'''

t1 = (1, 2,3 , 4,5)
single_ele = (23)
print(single_ele)
print(t1)

t1=(1, 2, 3, 4, 5, 6)
print(t1[0])
print(t1)
# t1[0]='s'
# print(t1)
co_ord = (10, 20)
x,y = co_ord
print(x, y)


n = (1, 2, 3, 4, 5)
a, b, *rest = n
a=10
b=20
a,b = b,a
print(a, b)


def min_max(num):
    return min(num), max(num)

res = min_max([1, 2, 3, 4, 5, 6])
print(res)

'''
1. find the index of the tuple with maximum value 
'''

'''
2. find the index of the tuple with the highest sum of elements
'''

tle = [(1,2), (3, 4), (5, 6), (7, 8)]
res = max(range(len(tle)), key=lambda i:sum(tle[i]))
print(res)

'''
coutn how many times each tuple appear in a list
'''
import collections as cs
lst = [(1, 2), (2, 3), (1, 2), (4, 5), (1, 2)]
res = cs.Counter(lst)
print(res)

'''
find the tuple with largest product of its elements
'''

# lst = [(1, 2), (3, 5), (2, 4)]
# max_pro=max(t1, key=lambda x:x[0]*x[1])
# print(max_pro)

'''
Given list of tuple where each tuple contain strings find the tuple with longest combined length of strings 
'''
lst = [('apple', 'banana'),('kiwi', 'cherry'), ('pineapple', 'orange')]
res = max(lst, key=lambda x:len(x[0])+len(x[1]))
print(res)

