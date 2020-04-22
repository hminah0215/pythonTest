a = [10,20,30]

#  예외가 발생할 상황에, 자바에서의 try, catch 예외처리처럼 
# 파이썬에서의 예외처리는 try: except:

try:
    print(a[0])
    print(a[5])
except IndexError:
    print("인텍스 범위를 넘었어요.")
except:
    print("예외발생")
finally:
    print("반드시 만나는 문장입니다.")