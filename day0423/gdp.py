import requests
import re

url = 'https://ko.wikipedia.org/wiki/%EC%9D%BC%EC%9D%B8%EB%8B%B9_%EB%AA%85%EB%AA%A9_%EA%B5%AD%EB%82%B4_%EC%B4%9D%EC%83%9D%EC%82%B0%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D'

text = requests.get(url).text
# print(text)
##mw-content-text > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(1)


f=open("day0423/gdp2019.csv", "w", encoding="UTF-8")

text = re.findall('<table class="wikitable sortable".+?>(.+?)</table>',text,  re.DOTALL)
text = text[0]
list = re.findall('<tr>(.+?)</tr>', text, re.DOTALL)
list = list[1:len(list)]
for line in list:
    data  = re.findall('<td>(.+?)</td>.+?<td.+?(.+?)</td>.+?<td>(.+?)</td>', line, re.DOTALL)
    rank, country, gdp = data[0]
    country= re.findall('title.+?>(.+?)</a>',country, re.DOTALL)
    gdp = gdp.replace(",","")
    if rank != "—":
        f.write(rank)
        f.write(",")
        f.write(country[0])
        f.write(",")
        f.write(gdp)


f.close()

print('파일을 생성하였습니다.')