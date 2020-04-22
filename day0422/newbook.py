import requests
import re

url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'

text = requests.get(url).text
list = re.findall('<li class="sub_book_list">(.+?)</li>', text, re.DOTALL)
n = 1
for book in list:
    img_url = re.findall('<img src="(.+?)" alt="" class="thumb" />', book)
    data = requests.get("https://www.hanbit.co.kr/"+img_url[0]).content
    fname = "book"+str(n)+".jpg"
    f = open("day0422/bookImg/"+fname, "wb")
    f.write(data)
    f.close()
    n= n +1
    print(n,"번째 그림을 다운 받았습니다.")



