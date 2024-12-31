'''
Numpy: 
    numerical computing 
    support for the multifunctional dimensions arrays and matrices
    It provides inbuilt statistical formulas
'''

import numpy as np 

#1D Array
a = np.array([1, 2, 3, 4, 5])
#2D Array
b = np.array([[1, 2, 3],[4, 5, 6]])

print(a)
print(b)

#reshaping work
reshape = b.reshape(3, 2) #array.reshape(rows, columns)
print(reshape)

#slice
slice = a[2:]
print(slice)

#find mean 
mean1=np.mean(b)
mean2=np.mean(a)
print(mean1, mean2)

#standard deviation
std1=np.std(b)
std2=np.std(a)
print(std1, std2)

#initializing array with zeros
zeros = np.zeros((2, 3))
print(zeros)

#initialize with Random number
rand=np.random.rand(3, 3)
print(rand)


#initialize with one
ones = np.ones((3, 4))
print(ones)


#create identity matrix
ident = np.eye(4)
print(ident)


#range of values
range_value = np.arange(10, 50, 5)
print(range_value)


#line space
line_space = np.linspace(0, 1, 5)
print(line_space)


#random integer initialization
rand_int = np.random.randint(1, 10, size=(2, 3))
print(rand_int)


#indexing and slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ele = arr[1, 2]
print(ele)
row = arr[1, :]
print(row)

#boolean indexing
bool_index=arr[arr>5]
print(bool_index)
col = arr[:, 1]
print(col)


#mathematical operations

#square
arr=np.array([1, 2, 3, 4, 5])
square = np.square(arr)
print(square)

#square root
sqrt = np.sqrt(arr)
print(sqrt)

#log
log = np.log(arr)
print(log)


#aggregate function

#sum and product
sum = np.sum(arr)
prod = np.prod(arr)
print(sum, prod)

#minimum and maximym
min = np.min(arr)
max = np.max(arr)
print(min, max)


#sum and product of 2 array

arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 4, 5])
sum_array = arr1+ arr2
prod_array = arr1*arr2
print(sum_array, prod_array)

#matrix dot operaion
dot = np.dot(arr1, arr2)
print(dot)


mat=np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])

#matrix tanspose
trns = mat.T
print(trns)

#calculate determinant
det = np.linalg.det(mat)
print(det)

#inverse of matrix
# inv = np.linalg.inv(mat)
# print(inv)

ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 5, 6])

#concat
con = np.concatenate((ar1, ar2))
print(con)


arr = np.array([1, 2, 3, 4, 5])
# np.save('arr.npy', arr)

arr = np.array([3, 2, 4, 5, 6])
sort = np.sort(arr)
print(sort)

arr1 = np.array([1, 2, 2, 2, 3, 3, 4, 4, 4])
res = np.unique(arr1)
print(res)


'''
Create a 5*5 matrix where all elements are zero
except the border, which should be 1.
'''

matrix = np.zeros((5, 5))
matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1
print(matrix)


'''
Generate an array of 100 random integers between
1 and 50 compute the mean of the nos greater than 25
'''

array = np.random.randint(1, 51, size=(1, 100))
filtered = array[array>25]
mean = np.mean(filtered)
print(mean)


'''
Given 3*3 matrix compute their element wise product and sum
'''


'''
Create a 1D array of 15 integers between 10 and 100
replace all numbers divisible by 3 with -1
'''


'''
Create a 6*6 matrix of rnadom integers between 1 and 20
extract all odd numbers , reshapes them into 3*2 matix
find the sum of its rows 
'''

'''
Create a 4*4 matrix with random integers between 1 and 10.
replace the diagonal element with their square
'''

mat = np.random.randint(1, 11, (4, 4))
np.fill_diagonal(mat, np.diagonal(mat)**2)
print(mat)


'''
Create an array of 20 random floats between 0 and 1
find the value closest to 0.5
'''

# mat = np.random.rand(1, 20)

# print(min, mat)


'''
create numpy array of 50 ranodm nos between 1 and 100
find all prime nos in array
for the prime nos compute their square root using ufunc

'''

#Universal functions
arr = np.array([1, 2, 3, 4, 5])
add = np.add(arr, 5)
print(add)
sub = np.subtract(arr, 1)
print(sub)
div = np.divide(arr, 2)
print(div)
sin = np.sin(arr)
cos = np.cos(arr)
tan = np.tan(arr)
exp = np.exp(arr)
print(sin, cos, tan, exp)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 6, 7, 8, 9])
bit = np.bitwise_and(arr1, arr2)
print(bit)

#round, floor