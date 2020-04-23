import numpy as np
import matplotlib.pyplot as plt

kor = [20,35,30,35,27]
eng = [25,32,34,20,25]
name = ["a","b","c","d","e"]


bar_width = 0.4
plt.bar(range(len(kor)), kor, bar_width)
plt.bar(np.arange(len(kor))+bar_width, eng, bar_width)
plt.xticks(np.arange(len(kor)) +bar_width/2, name )
plt.show()



# x = np.linspace(-10,10,100)
# y = np.sin(x)
# # plt.plot(x,y,"ro")
# plt.plot(x,y,marker="x")
# plt.show()
# # print(x)
# # print(y)



#연습)
#x의 범위가 -10에서 10일때 x의제곱을 차트로 표현해 주세요.
# x = np.arange(-10,10+1,0.1)
# y = x ** 2
# plt.plot(x,y,"ro")
# plt.show()


# a = np.arange(10)
# b = np.arange(1,10)
# c = np.arange(1,10,2)
# print(a)
# print(b)
# print(c)


# x = np.array([1,2,3,4,5])
# y = np.array([1,4,6,8,10])
#
# # print(x.max(),x.min())
# # print(y.max(),y.min())
#
# plt.plot(x,y,"ro")
# plt.xlim(x.min()-1,x.max()+10)
# plt.ylim(y.min()-1,y.max()+10)
# plt.show()


# math = [80,90,100,40,90]
# eng = [100,90,100,50,100]
#
# plt.plot(math, eng, "ro")
#
# # plt.plot(math)
# plt.show()