set1 = set()
s1 = {1, 2, 3, 4, 5, 6}

s1.add(7)
print(s1)

s1.remove(4)
print(s1)

# s1.discard()
s1.clear()

s2={1, 2, 3}
s3={3, 4, 5}
#union
print(s2 | s3)
print(s2.union(s3))

#intersection
print(s2&s3)
print(s2.intersection(s3))

#difference
print(s2^s3)
print(s2.difference(s3))
print(s2.symmetric_difference(s2))

'''
Removing duplicates from list 
'''

lst = [1, 2, 2, 3, 4, 4, 5]
set1=set(lst)
l1=list(set1)

"""
Finding the common element between two lists
"""

l1 = [1, 2, 3]
l2 = [2, 3, 4]
set1 = set(l1)
set2 = set(l2)
com_set = set1&set2
com_list = list(com_set)
print(com_list)

'''
find the unique elements from 2 lists
'''
l1 = [1, 2, 3]
l2 = [2, 3, 4]
set1 = set(l1)
set2 = set(l2)
com_set = set1^set2
com_list = list(com_set)
print(com_list)

'''
classes with the following students list
'''

classA = {
    'Alice', 'Bob', 'Charlie', 'David'
}
classB = {
    'Charlie', 'David', 'Eve', 'Frank'
}
classC = {
    'David', 'Frank', 'Grace', 'Bob'
}

'''
Students who are in all 3 classes
'''


'''
Students who are in atlest one classes
'''


'''
Students who are in exactly two classes
'''


