# 임의의 수 n을 입력받아 1-n까지의 합을 누적하여 출력해봅니다. 
""" n = int(input("숫자를 입력하세요 ==> "))
sum = 0
i = 1
while i <= n :
    sum = sum + i
    i = i + 1
print (sum) """

#range(시작값, 최종값, 증강값..은 생략가능)
""" for i in range(1,10,1) :
    print("hello") """

""" for i in range(1, 10, 1) :
    print(i, end=" ") 
#결과, 1 2 3 4 5 6 7 8 9     
"""

""" for i in range(10) :
    print(i, end=" ")
# 결과, 스타트를 생략해서 0부터 나옴 , 0 1 2 3 4 5 6 7 8 9  """

# 임의의 수 n을 입력받아 1-n까지의 합을 누적하여 출력해봅니다. for사용! 
""" n = int(input("숫자를 입력하세요 ==> "))
tot = 0
for i in range(1, n+1) :
     tot = tot + i
print(tot) """

# 연습) 0~9사이의 수를 거꾸로 출력해 봅니다. (for문 이용)
""" for i in reversed(range(0,10,1))  : 
    print(i, end =" ")
#end = " " 블랭크하면 옆으로 출력    
 """
""" for i in range(9, -1, -1) :
    print(i, end=" ")
#결과, 9 8 7 6 5 4 3 2 1 0  """

data = [10,20,30,40,50]
""" for v in data :
    print(v, end=" ") """
    
# 연습) data의 요소를 거꾸로 출력해봅니다.
""" for v in reversed(data) : 
    print(v, end=" ") """

print(list(reversed(data)))

""" # 이 방식은 자바사용의 습관! 파이썬에선 reversed 를 쓰는게 더 유용하다.
for i in range(len(data)-1,-1 ,-1):
    print(data[i], end =" ") """