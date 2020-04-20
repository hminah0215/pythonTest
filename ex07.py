# 정규표현식 사용, 파이썬에서는 re 라는 내장 라이브러리가 존재한다.
import re

# 파이썬에서 많은 문자열을 입력할때는 홑따옴표 ''' 3개 사이에 넣어야한다.
db =''' 3412    Bob 123
        3834  Jonny 333
        1248   Kate 634
        1423   Tony 567
        2567  Peter 435
        3567  Alice 535
        1548  Kerry 534
        1234  Tiger 321'''
# 연습) T로 시작하는 이름만 출력해봅니다. 
tname = re.findall('T[a-z]+',db)
print(tname)

# 연습 ) T로 시작하지 않는 이름만 출력해봅니다.
#notT = re.findall('[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+',db)
notT = re.findall('[A-SU-Z][a-z]+',db)
print(notT)

# 연습) 전화번호만 출력합니다.
""" telList = re.findall('[0-9]{4}',db)
print(telList) """

# 연습) id만 출력합니다.
""" idList = re.findall('[0-9]{3}$',db, re.MULTILINE)       #re.MULTILINE ,데이터가 여러줄에 걸쳐있다고 옵션을 추가 
print(idList) """

# 연습 ) 이름만 출력해봅니다.
# []+ , 여기서 + 는 적어도 한글자 이상인것
""" names = re.findall('[A-z]+',db)
print(names) """

# 전화번호와 id를 모두 출력해 봅니다.
""" r = re.findall('[0-9]+',db)  #db로부터 이런 패턴(숫자인것)을 가진 걸 찾아주세요.
print(r) """

# print(db)
