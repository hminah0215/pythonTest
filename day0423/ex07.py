import numpy as np

a = np.arange(3)
b = np.arange(6)
c = a.reshape(3,-1)
d = a.reshape(-1, 3)
e = b.reshape(3,-1)
f = b.reshape(-1,3)

# 일차원 배열의 2차원 배열을 연산을 할 때에는
#    열의 크기를 맟추어 주거나
#    1열의 데이터로 맞추어 줍니다.

# print(b)
# print(f)
# print(b+f)      #오류

# [0 1 2 3 4 5]
# [[0 1]
#  [2 3]
#  [4 5]]
# print(b)
# print(e)
# print(b+e)        오류 발생


# [0 1 2 3 4 5]
# [[0 1 2]]
# print(b)
# print(d)
# print(b+d)        오류


# print(b)
# print(c)
# print(b+c)
# [0 1 2 3 4 5]
# [[0]
#  [1]
#  [2]]
# [[0 1 2 3 4 5]
#  [1 2 3 4 5 6]
#  [2 3 4 5 6 7]]



#       1차원 배열와 2차원 배열의 연산
#           ==>1차원 배열의 열의 수와 2차원의 배열의 열의 수가 같을 때는 연산이 가능합니다.
#               2차원의 배열의 shape과 동일하고
#               1차원 배열이 2차원 배열의 행의 수 만큼 연산합니다.
#           ==> 1차원 배열의 모양이 (n,)이고 2차원 배열의 모양이 (n,1) 이거나
#                       생성되는 shape이 (n,n)
#           ==>                           2차원 배열의 모양이 (1,n)일때 연산이 가능합니다.
#                       생성되는 shape이 (1,n)로 생성이 됩니다.


# print(a)
# print(f)
# [0 1 2]
# [[0 1 2]
#  [3 4 5]]

# [[0 2 4]
#  [3 5 7]]
# print(a+f)


# print(a)
# print(e)
# [0 1 2]
# [[0 1]
#  [2 3]
#  [4 5]]
# print(a+e)            오류


# print(a)
# print(d)
# # [0 1 2]
# # [[0 1 2]]
# print(a+d)


#a+c            1차원 배열의 열의 수와(n) 2차원 배열의 행의 수(m)가 동일할 때 연산이 가능합니다.
#               생성되는 2차원 배열의 shape(m,n)
#  [0 1 2]
# [[0]
#  [1]
#  [2]]
# print(a)
# print(c)
# print(a+c)
# [0 1 2]
# [[0]
#  [1]
#  [2]]
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]



#각각의 요소를 더하기 해 봅니다.
#[0 1 2]
#[0 1 2 3 4 5]
# print(a)
# print(b)
# print(a+b)        오류



# data = [10,20,30,40,50,60,45,50]
# a = np.array(data)
# print(a.size)
#
# b = a.reshape(-1, a.size)
# c = a.reshape(a.size, -1)
# print("데이터를 이차원 배열의 열의 요소로 표현")
# print(b)
# print("="*50)
# print("데이터를 이차원 배열의 행의 요소로 표현")
# print(c)


# #1차원의 배열
# a = np.arange(3)
#
# #1행 3열로 표현
# b = a.reshape(-1,3)
#
# #3행 1열
# c = a.reshape(3,-1)
# print(a)
# print(b)
# print(c)

# a = np.arange(5)
# b = a.reshape(-1,3)
# print(b)

# a = np.arange(6)
# b = a.reshape(2,-1)
# print(b)
# b = a.reshape(-1,3)
# print(b)
# b = a.reshape(2,3)
# print(b)




# #1차원 배열끼리 size가 다르면 연산을 할 수 없어요!
# a = np.arange(10)
# b = np.arange(5)
# print(a)
# print(b)
# print(a+b)


# a = np.arange(9)
# b = np.arange(10,100,10)
# print(a)
# print(b)
# print(a+b)

# a = np.arange(6)
# print(a)
# print(a+10)


# a = np.array([1,2,3,4,5])
# b = a ** 2
# print(b)
