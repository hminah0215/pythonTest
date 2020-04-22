import requests
import re

url = 'https://www.hanbit.co.kr/data/books/B8977162495_m.jpg'

data = requests.get(url).content
f = open("book.jpg","wb") #텍스트가 아닌 이미지를 저장하려는거라 wb 바이너리 타입이란것도 적어줘야한다. 그냥 w는 텍스트만 
f.write(data)
f.close()
print("이미지를 다운받았습니다.")