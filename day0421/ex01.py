import re
import requests

url ='https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
text = requests.get(url).text
#print(text)



#   city, 날짜, 날씨, 최고온도, 최저온도를 출력해보세요.
#   00시 12시 두개가 있는데 그중 12시 데이터만 나타나도록 해보세요.

loc = re.findall('<location wl_ver="3">(.+?)</location>',text,re.DOTALL)   #원하는 데이터가 여러줄에 걸쳐져있을때 re.DOTALL 사용
f = open('Data/weather3.txt','w',encoding="utf-8")

arr = []

for location in loc:
    city = re.findall('<city>(.+?)</city>',location)[0]
    data_list = re.findall('<data>(.+?)</data>',location,re.DOTALL)
    
    for data in data_list:
        date = re.findall('<tmEf>(.+?)</tmEf>',data)[0]
       # print(date[0].find("12:00"))    #없으면 -1
        if  date.find('12:00') !=  -1 :
            weather = re.findall('<wf>(.+?)</wf>',data)[0]
            tmx = re.findall('<tmx>(.+?)</tmx>',data)[0]
            tmn = re.findall('<tmn>(.+?)</tmn>',data)[0]
            #print(city,date,weather,tmx,tmn)

            arr.append({"city":city, "date":date,"weather":weather,"tmx":tmx,"tmn":tmn})


  # 도시명, 날짜, 날씨, 최고온도, 최저온도를 파일로 저장해봅니다. 
            #f_list = [str(city), str(date), str(weather), str(tmx), str(tmn),"\n"]
            #f.writelines(f_list)

            # 위처럼 할때는 for data[0] in data_list 로 루프를 돌아야함, city등 다른곳의 맨뒤의 [0]은 지워주고!

            # f.write(city+"/")
            # f.write(date+"/")
            # f.write(weather+"/")
            # f.write(tmx+"/")
            # f.write(tmn+"\n")
f.writelines(str(arr))
f.close
print("파일을 기록하였습니다.")
