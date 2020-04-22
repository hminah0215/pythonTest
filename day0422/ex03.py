import requests
import re

url = 'https://www.hanbit.co.kr/data/books/B9288599157_m.jpg'

data = requests.get(url).content
f = open("book", "wb")
f.write(data)
f.close()
print("이미지를 다운받았습니다.")