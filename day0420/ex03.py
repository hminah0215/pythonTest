# a,b = 5,2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b) #나누기 할때 // 이렇게 두번을 쓰면 정수로 출력
#
# print(a**b)  #a의 b제곱

#연습
#두자리 양수를 거꾸로 뒤집어 보세요.
#71 ---> 17

# a = 71
# print(a%10,a//10)

# 비교연산자
# > >= < <= == !=

# a,b = 3,7
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)

# n = input("숫자를 입력하세요")
# print(n)

#연습
#사용자에게 임의의 수 n을 입력받아 그 수가 10과 20사이의 수 이면 true를 출력하고
#그렇지 않으면 false를 출력합니다.

# n = input("숫자를 입력하세요")
# n = int(n)
# # print(n >= 10 and n <= 20)
# print(10 <= n <=20)     #파이썬은 이렇게 입력하는것도 가능하다

n = 12 
print(int(n >= 100))     #false 를 int로 변환해서 0
print(n >= 10 * n <= 20) #false 출력된다. 곱하기 먼저 실행되니 10*12가 20보다 작은지 먼저 판별하기때문

print( (n >= 10) * (n <= 20) ) 
