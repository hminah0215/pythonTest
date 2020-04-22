import requests
import re

def getNewBook():
    arr = []

    url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'

    # 이미지이름을 도서명으로 저장해 봅니다.
    text = requests.get(url).text
    list = re.findall('<li class="sub_book_list">(.+?)</li>', text, re.DOTALL)

    for book in list:
        img_url = re.findall('<img src="(.+?)" alt="" class="thumb" />', book)
        data = requests.get("https://www.hanbit.co.kr/" + img_url[0]).content
        bookname = re.findall('<p class="book_tit"><a href=".+?">(.+?)</a>', book)
        bookname = bookname[0].replace("&#40;", "_")
        bookname = bookname.replace("&#41;", "_")
        fname = bookname + ".jpg"
        #리팩터링 2판 &#40;리팩토링 개정판&#41;.jpg

        f = open("C:/_Study/pythonTest/static/" + fname, "wb")
        f.write(data)
        f.close()

        price = re.findall('<span class="price">(.+?)<span>원</span>', book)
        arr.append({"title":bookname, "price":price[0]})
    return arr