import numpy as np
#create an array with numpy
a = np.array([1,2,3])
print(a) #print array
print(type(a)) #type
print(a.shape) #prints number of dimensions, in this case (3,)

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0]) 


#Create different arrays

a = np.zeros((2,2)) #array of all zeros, 2 rows, 2 columns

b = np.ones((2,2)) #array of all ones, 2 rows, 2 columns

c = np.full((2,2), 7) #array of 7, 2 rows, 2 columns

d = np.eye((2)) #2x2 identity matrix

e = np.random.random((2,2)) #an array of random values between 0 and 1

#array slicing

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b= a[:2,1:3]
print(b)
