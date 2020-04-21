import re
import requests

url ='https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
text = requests.get(url).text
#print(text)

# 모든 province를 출력해봅니다.
list = re.findall('<province>(.+?)</province>',text)
print(len(list))
#print(list)

#city, 날짜, 날씨, 최고온도, 최저온도를 출력해보세요.
city = re.findall('<city>(.+?)</city>',text)
date = re.findall('<tmEf>)(.+?)</tmEf>',text)
weather = re.findall('<wf>(.+?)</wf>',text)
tmx = re.findall('<tmx>(.+?)</tmx>',text)
tmn = re.findall('<tmn>(.+?)</tmn>',text)
print(city)
print(date)
print(weather)
print(tmx)
print(tmn)
