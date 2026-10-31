import numpy as np

# # Python list
# a = [1, 2, 3]
# print(a * 2)

# # NumPy array
# b = np.array([1, 2, 3])
# print(b * 2)

# import numpy as np

# arr = np.array([10, 20, 30, 40])

# print(arr)
# print(type(arr))    

# import numpy as np
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)

# np.zeroes((2,3))

# np.ones((2,2))


# arr=np.array([[10,20,30],[40,50,60]])
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)

# arr=np.array([10,20,30,40,50])
# print(arr[0])
# print(arr[2])
# print(arr[-1])

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(arr[0, 0])  # 10
# print(arr[0, 2])  # 30
# print(arr[1, 1])  # 50

# Sytax for Slicing arr[start:stop:step]


# arr = np.array([10, 20, 30, 40, 50])

# print(arr[1:4])   # [20 30 40]
# print(arr[:3])    # [10 20 30]
# print(arr[2:])    # [30 40 50]
# print(arr[::2])   # [10 30 50]
# print(arr[::-1])  # [50 40 30 20 10]

# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])

# print(a + b)  # [11 22 33]
# print(a - b)  # [ 9 18 27]
# print(a * b)  # [10 40 90]
# print(a / b)  # [10. 10. 10.]
# print(a ** 2) # [100 400 900]
# print(a % b)  # [0 0 0]

# arr = np.array([1, 2, 3])

# print(arr + 5)  # [6 7 8]
# print(arr * 3)  # [3 6 9]

# print(np.zeros(4))
# print(np.ones((4),dtype=int))
# print(np.full(3,7))
# print(np.empty(4))

# arr=np.array([1,4,9,16])
# print(np.sqrt(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.std(arr))

# arr=np.array([10,20,30,40,50])
# print(arr>20)
# # print(arr== 30)
# [False False  True  True]
# [ True False False False]

# arr=np.array([10,20,30,40,50])
# print(arr[arr>25]) [30 40 50]

# create a numpy arr conatains 1st 10 natural no and display it
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr)
# arr = np.arange(1, 11)
# print(arr)
# print(len(arr))

# datatypes in numpy(dtype)
# print(np.array([1,2,3,4]).dtype)
# print(np.array([1.0,2.3,3,4]).dtype)

# x=np.array([1,2,3],dtype=float)
# print(x)

# y=np.array([1.7,2.9]).astype(int)
# print(y)

# print(np.array([1,5,6]).astype(bool))

# m=np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(m[0,-1])
# print(m[0,2])
# print(m[-1,-1])
# print(m[1,2])

# x=np.arange(12)
# print(x.reshape(3,4))
# print(x.reshape(2,-1).shape)
# print(x.reshape(3,4).flatten())
# print(x.reshape(3,4).T.shape)
# try:
#     x.reshape(5,3)
# except ValueError as e:
#     print(e)

