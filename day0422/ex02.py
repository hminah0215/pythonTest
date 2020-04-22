list = [10,20,30,"사과"]

for n in list:
    try:
        print(n+2)
    #하지만, 당연히 이렇게 스트링자료형이 있다면 연산을 할 수 없으므로 예외처리 
    except TypeError:
        print("숫자가 아닙니다.")

''' print(list)
print(type(list))

for data in list:
    print(data)
    print(type(data)) '''

''' 실행결과, 다양한 자료형을 담을 수 있다.
[10, 20, 30, '사과']
<class 'list'>
10
<class 'int'>
20
<class 'int'>
30
<class 'int'>
사과
<class 'str'> '''
