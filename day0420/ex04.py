# 어떤수가 홀수인지 짝수인지 판별하여 출력
""" a = 3
if  a % 2 == 0 :
    print("짝수")
else :
    print("홀수") """

# 사용자에게 임의의 수 n을 입력받아 음수인지, 양수인지, 0 인지 판별하여 출력합니다.
n = input("숫자를 입력하세요.")
n = int(n)

if n % 2 == 0 and n != 0:
    print("짝수")
elif n % 2 != 0 :
    print("홀수")
elif n == 0 :
    print("0입니다.")
