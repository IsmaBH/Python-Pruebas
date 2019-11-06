import numpy as np

#Ejemplos de creacion de arrays desde objetos propios de python
my_list = [1,2,3]
arr = np.array(my_list)
print(arr)
my_mat = [arr,arr,arr]
matrix = np.array(my_mat)
print(matrix)
#Metodos de creacion propios de numpy
#Syntax of arange(): np.arange(start, stop, step, dtype)
#start: Start of an interval, default value is 0 (opcional)
#Stop: end of the interval
#Step: is an optional number and can't be 0
#dtype: IS the type of the output array, if not given the type will bi infer from the other inputs
arr2 = np.arange(0,25)
#Linspace
np.linspace(0,5,1)
#rand
np.random.rand(5)
np.random.rand(5,5)
#randn
np.random.randn(4,4)
#randint
arr3 = np.random.randint(1,50,10)
#Methods
#CAn change a 1 dimension array into a 2 dimension array
arr2.reshape(5,5)
#Finds the max value in the array
arr3.max()
#Finds the min value in the array
arr3.min()
#Finds the index of the maximum value
arr3.argmax()
#Finds the index of the min value
arr3.argmin()
#Tells the shape of the arrray
arr3.shape
#Tells the data type of the array
arr3.dtype
#Indexing and Selection
arr4 = np.arange(0,9)
print(arr4[8])
print(arr4[1:5])
print(arr4[:6])
print(arr4[5:])
#This is important because, when we do "arr = arr4[2:4]" we are not copying the values
#we are passing a reference to the original and if we change "arr" we'll change the
#original too so if we want a copy use the method below
arr_copy = arr4.copy()
#Matrix
arr_2d = arr_copy.reshape(3,3)
#Double bracket notation
arr_2d[0][1]
#Coma notation
arr_2d[1,2]
#Selection
arr_2d[:2,1:]
#Conditional selection
arr_2d[arr_2d<3]
#Operations