
""" n = 0
while True :
    print("hello")
    n = n + 1
    if n == 3 :
        break """

# 연습
# 사용자에게 정수를 입력받아 그 수가 몇자리 수 인지 판별하여 출력합니다(이번엔 반복문이용)

n = int(input("숫자를 입력하세요 ==> "))
cnt = 0
while True :
    n = n // 10
    cnt = cnt + 1
    if n == 0 :
        break
print (cnt)


# 연습 
# 0~9999 사이의 정수를 입력받아 그 수가 몇자리 수 인지 판별하여 출력합니다.

#  n = int(input("0~9999 사이의 숫자를 입력해주세요. ==>"))

""" if 0 <= n <= 9999 : 
    if n < 10 : 
        print(1)
    elif n < 100 :
        print(2)
    elif n < 1000 :
         print(3)
    elif n < 10000 : 
         print(4)
else :
    print("숫자를 다시 입력해주세요.")  """


""" if 0 <= n <= 9999 : 
    if 0 <= n <= 9 : 
      print(1)
    if 10 <= n <= 99 :
        print(2)
    if 100 <= n <= 999 :
     print(3)
    if 1000 <= n <= 9999 : 
     print(4)
else :
    print("숫자를 다시 입력해주세요.") """