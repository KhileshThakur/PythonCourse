'''
list: 
-Mutable
-Ordered collection of items
-versatile data structure
-store elements of any data type

'''

li=[1, 2, 4.5, 'siri']
nested_list = [1, 2, [3, 4, 5], 6, 'hello']

#list object

s=list(range(1,6))
print(s)

l1 = [10, 20, 30, 40, 50]
print(l1)
print(l1[0])
print(l1[-1])
l1[1]=24
print(l1)

#slice
print(l1[1:3])
print(l1[:3])
print(l1[::2])

fruits = ["Apple", "Mango", "Orange", "Cherry"]
fruits.append("Banana")
print(fruits)
fruits.insert(2, "Pineapple")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

n=[1, 2, 3]
res=n+[4, 5, 6, 7]
print(res)
rep = n*3
print(rep)
n= [1,2,3,4,5]
print(2 in n)
print(3 not in n)
print(len(n))





letters = ['a', 'b', 'c', 'a', 'b', 'a']
print(letters.count('a'))
print(letters.index('b'))
letters.extend(['d', 'e'])
print(letters)

copy_var = letters.copy()
print(copy_var)

for index, ele in enumerate(letters):
    print(f"{index+1} : {ele} ", end="")
    

#Nested list

nested = [[1, 3, 4], [4, 5, 6], [6, 3, 6]]
print(nested[1][2])



#Questions : 

'''
generate 1 to 5 Numbers and square them
'''

res = [x**2 for x in range(1, 6)]
print(res)

'''
square of only even no for prev ques
'''

res1 = [x**2 for x in range(1, 6) if x%2==0]
print(res1)


'''
Group the identical elements in a list
'''

list_with_identical = [1, 1, 2, 3, 3, 3, 4, 4, 5] #output => [[1, 1],[2],[3, 3, 3], [4, 4], [5]]
ls_grouped = []
for item in list_with_identical:
    if not ls_grouped or ls_grouped[-1][0] != item:
        ls_grouped.append([item])
    else:
        ls_grouped[-1].append(item)
print(ls_grouped)


'''
Interleave the elements of two lists
'''

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']
#op ==> [1, 'a', 2, 'b, 3, 'c', 'd']

merged = [item for i in zip(l1, l2) for item in i]+l2[len(l1):]
print(merged)

'''
Find the duplicates in a list
'''

l3 = [1, 2, 3, 4, 5, 3, 2, 6, 7]
duplicates = [x for x in l3 if l3.count(x) > 1]
print(duplicates)
duplicatenew = set(duplicates)
print(duplicatenew)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
res = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(res)