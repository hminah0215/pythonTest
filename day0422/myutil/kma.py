import requests
import re

def getData():
    arr = []
    # 도시명, 날짜, 날씨, 최고온도, 최저온도를 파일로 저장해 봅니다.
    url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'

    text = requests.get(url).text
    # print(text)

    list = re.findall('<location wl_ver="3">(.+?)</location>', text, re.DOTALL)
    # json 형태로 출력해 봅니다.
    for location in list:
        city = re.findall('<city>(.+?)</city>', location)[0]
        data_list = re.findall('<data>(.+?)</data>', location, re.DOTALL)
        for data in data_list:
            tmEf = re.findall('<tmEf>(.+?)</tmEf>', data)[0]
            if tmEf.find("12:00") != -1:
                wf = re.findall('<wf>(.+?)</wf>', data)[0]
                tmx = re.findall('<tmx>(.+?)</tmx>', data)[0]
                tmn = re.findall('<tmn>(.+?)</tmn>', data)[0]
                arr.append({"city":city, "tmEf":tmEf, "wf":wf,"tmx":tmx,"tmn":tmn})
    return arr