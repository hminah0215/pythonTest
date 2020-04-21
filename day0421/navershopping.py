import re
import requests
def saveFile(search, fname):
    fname = search 
    f = open("Data/naver2.txt", "w", encoding="utf-8")
    search = '아스프라거스'
    url = 'https://search.shopping.naver.com/search/all.nhn?query='+search+'&cat_id=&frm=NVSHATC'
    text=requests.get(url).text
    list = re.findall('<div class="info">(.+?)<span class="depth">', text, re.DOTALL)
 
    arr = []

    for line in list:
        if len(line) < 2000:
            url = re.findall('<div class="tit">.+?<a href="(.+?)" class="link"', line, re.DOTALL)
            price = re.findall('class="num _price_reload".+?>(.+?)</span>원</em>', line)
            title = re.findall('title="(.+?)">.+?</a>', line)
            print(title, url, price)
            arr.append({"title":title[0], "url":url[0], "price":price[0]})
            print("="*50)

    f.writelines(str(arr))
    print(search + "를 검색하여"+fname+"으로 저장하였습니다.")
    f.close()