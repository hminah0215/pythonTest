import requests
import re

# 연습) 알라딘 홈페이지, 새로나온 도서 중에 프로그래밍 언어관련 도서의 
#       도서명, 출판사, 저자, 가격의 정보를 수집하여 출력합니다.
#       단, 2020냔 4월 출간도서만 출력하세요.

url ='https://www.aladin.co.kr/shop/common/wnew.aspx?NewType=SpecialNew&BranchType=1&CID=437'
data = requests.get(url).text
 
april = re.findall("[2020년 4월]",data)
while True:
    title = re.findall('class="bo3"><b>(.+?)</b>',data)
    publisher = re.findall("&BranchType=1' >(.+?)</A>",data)
    author = re.findall('AuthorSearch=(.+?)@',data)
    price = re.findall('<span class="ss_p2" ><b><span class="">(.+?)</span>',data)
    break
print(title)
print(publisher)
print(author)
print(price)