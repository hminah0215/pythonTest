import  requests
import re
def saveFile(search):
    fname = search+".txt"
    f = open(fname, "w", encoding="utf-8")
    url = 'https://search.shopping.naver.com/search/all.nhn?query=' + search + '&cat_id=&frm=NVSHATC'
    text = requests.get(url).text
    list = re.findall('<div class="info">(.+?)<span class="depth">', text, re.DOTALL)
    arr = []
    for line in list:
        if len(line) < 2000:
            url = re.findall('<div class="tit">.+?<a href="(.+?)" class="link"', line, re.DOTALL)
            price = re.findall('class="num _price_reload".+?>(.+?)</span>원</em>', line)
            title = re.findall('title="(.+?)">.+?</a>', line)
            # url = re.findall('class="link"', line)
            print(title, url, price)
            arr.append({"title": title[0], "url": url[0], "price": price[0]})
            print("=" * 50)

    f.writelines(str(arr))
    print(search + "를 검색하여 " + fname + "으로 저장하였습니다.")
    f.close()

# saveFile('기미크림')