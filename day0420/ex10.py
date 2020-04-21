import requests
import re

url = 'http://libseat.sogang.ac.kr/seat/roomview5.asp?room_no=2'
data = requests.get(url).text
text = bytes(data,'iso-8859-1').decode("euc-kr")

title = re.findall('<FONT SIZE="4"><B>(.+?)</B></FONT>',text)
print(title)    #['서강대학교 로욜라도서관 열람실별 실시간 좌석 정보'] 

# 연습) 총 좌석수를 출력해봅니다. 
# ['65'] 출력
seats = re.findall("<font color=blue><b>(.+?)</b></font></td>",text)
print(seats)