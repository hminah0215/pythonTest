import re
import requests
#   NAVER 쇼핑에서 '아스파라거스' 검색한 결과에서 
#   상품명, 가격, URL을 json파일로 기록해봅니다.

# str = "hello java"
# r = re.findall('korea$', str)
# print(r)

f = open("Data/naver.txt", "w", encoding="utf-8")


search = '아스프라거스'
url = 'https://search.shopping.naver.com/search/all.nhn?query='+search+'&cat_id=&frm=NVSHATC'
#'코스트코 냉동 그린 아스파라거스 1kg'
text=requests.get(url).text
list = re.findall('<div class="info">(.+?)<span class="depth">', text, re.DOTALL)
# for line in list:
#     print(len(line))
#     # r = re.findall('</span>$', line, re.DOTALL)
#     # print(r)
#     print("="*50)

arr = []

for line in list:
    if len(line) < 2000:
        url = re.findall('<div class="tit">.+?<a href="(.+?)" class="link"', line, re.DOTALL)
        price = re.findall('class="num _price_reload".+?>(.+?)</span>원</em>', line)
        title = re.findall('title="(.+?)">.+?</a>', line)
        # url = re.findall('class="link"', line)
        print(title, url, price)
        arr.append({"title":title[0], "url":url[0], "price":price[0]})
        print("="*50)

f.writelines(str(arr))
print("데이터를 수집하였습니다.")

'''
<div class="tit">
            <a href="https://cr2.shopping.naver.com/adcrNoti.nhn?x=%2Bz5vmGaOcQGT5THVHbIbhf%2F%2F%2Fw%3D%3Dsa3JmLMkMxyo%2FPTe7%2B5DDvhygfCRaRpwFSf7atp7N9NQaFiw0ntL025pzNJnTbuIvCH2tZUcUwsNUYDjMfvOmiDnHXz4thvXCAgUqFbzMve4mD2x4LzdBC5zPlSjIDqnAqHISpj5LLb1PcO8KK0Jfk2CXhjdj4H46FEnwGU8yP3%2BW3IGKHTcCAQcnIH8DpDXPS6IIWGZE0SomcLzzQE0fsRphtfhSkUdTWF%2FV2OTxY4G98pgsmewAbJ%2BA2UFZwIRxR0ckDRv5P8jHVuyzl1WtDP50EdV0NULWKtHs0s5GeRRKxQ86B9zxmnvILsKESGzWIrPQoQoZAMHn3vYtzQxVX2oh3MvOfpp2FwdLOtQe09sb7VizCqezlc4vsFbXfnti4LBYhASul5xoHn6kheqgcBkaKX7pTvXs6WG1e2oAbVUO8uoL%2FTYJZItlpHXifHeg%2BPisnnZGP3x1D%2FQ2Mk9g2M6AXJ5gzkgiRb4xdihRWRTBtdPoPKWE1r4%2BHIvyezq6XVDadGPopvKJmthgvsFORJUtpzZN0sg6%2BOeILGUY2BInp7iZhKeFHAK4aThY3rBZaDMSpEgHENOYjtyOPDDoZsJtBA1p5MyFtJy5ll50RchYOFjNzAftMReknJIuUCHjOw1aWlnZ6Nek4UdeoTBOeNg%2FTggpTz4gx%2FJoT6w%2BtaRRg9Ex5ufdgh%2FbQKYc7wkFiykOpMxd%2BOWY3PJRGf55ARlOSxfhgWwdYmPzIqFzxPk6c0xkPqwaQd1rA7iKRH9o&nv_mid=16520458111&cat_id=50002229" class="link" target="_blank" 
            title="아스파라거스 500g">아스파라거스 500g</a>
            <!-- N=a:lst*N.title,i:16520458111,r:28 -->
        </div>
        <span class="price">
				<em><span class="num _price_reload" data-reload-date="2020.04.21.">8,000</span>원</em>
                    </span>
'''

