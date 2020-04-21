""" def pro():
    print("hello")

pro() """

""" def pro(a,b):
    print(a)
    print(b)

pro(2,3) """

# 연습) n을 전달받아 1에서 n까지의 합을 누적하여 출력하는 함수를 정의하고 호출해봅니다.
""" def sumN(n):
    r = 0
    for i in range(1,n+1,1):
        r = r + i
    return r
tot = sumN(10)
print(tot)   
 """

# 연습) 두 수를 매개변수로 전달받아 그 중에 큰 수를 반환하는 함수를 정의하고 호출해봅니다.
""" def max(a, b):
    if b > a:
        a = b
    return a

print(max(2, 3)) """

# 연습) 4개의 수를 전달받아 그중에 큰 수를 찾아 반환하는 함수를 만들고 호출해봅니다.
""" def max4(a,b,c,d):
    return max(max(max(a,b),c),d)
print(max4(100,3,5,9)) """


""" def max4(a, b, c, d):
    return max(max(a, b), max(c, d))
print(max4(100, 3, 5, 9)) """

# 파이썬에서는 함수가 여러개를 리턴할 수 있다.
""" def pro():
    return 10,20,30 """

# 결과 : 10 20 30
""" a,b,c = pro()
print(a,b,c) """

#(10, 20, 30)
#<class 'tuple'> 바꿀 수 없는 자료형 , 리스트의 상수버전
""" r = pro()
print(r)
print(type(r)) """

# 대괄호로 묶이면 리스트, 소괄호로 묶이면 튜플

#<class 'list'> 변경이 가능한 자료형
#[10, 20, 30]
""" a = [10,20,30]
print(type(a))
print(a) """


# 연습) n을 매개변수로 전달받아 1~n까지의 합, n의 제곱, n*2를 차례로 반환하는 함수를 정의하고 호출해봅니다.
def multi(n):
    tot = 0
    for i in range(1,n+1,1):
        tot = tot + i
    return tot, n*n, n*2

tot, r1, r2 = multi(5)
print(tot,r1,r2)
# 위는 소괄호 없이 15 25 10, 아래는 (15, 25, 10) 이렇게 출력된다.
""" r = multi(5)
print(r) """
    
    
 

