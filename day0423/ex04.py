import numpy as np 

a = np.arange(6)
print(a)

# [0 1 2 3 4 5]

b = list(a)
print(b)           # [0, 1, 2, 3, 4, 5]
print(type(a))      #<class 'numpy.ndarray'>
print(a.shape)      #(6,)       차원확인

b = a.reshape(2,3)
print(b)            
print(b.shape)

# [[0 1 2]
#  [3 4 5]] 
# (2, 3)    차원 바꿔줌

print(a.size)
print(b.size)

# 몇차원인지 알 수 있음 
print(a.ndim)
print(b.ndim)

# a = np.arange(5)
# print(a)  #[0 1 2 3 4]

# b = np.arange(1,10)
# print(b)    #[1 2 3 4 5 6 7 8 9]

# c = np.arange(0,100,10)
# print(c)    #[ 0 10 20 30 40 50 60 70 80 90]

# d = np.arange(100,0,-10)
# print(d)    #[100  90  80  70  60  50  40  30  20  10]

