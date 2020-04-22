import re
import requests

url = "https://comic.naver.com/webtoon/weekday.nhn"

text = requests.get(url).text
list = re.findall('<div class="col_inner">(.+?)</ul>', text, re.DOTALL)
for line in list:
    li = re.findall("<li>(.+?)</li>", line, re.DOTALL)
    for data in li:
        a = re.findall('src="(.+?)".+? title="(.+?)"', data, re.DOTALL)
        img_url, title = a[0]
        content = requests.get(img_url).content
        #f = open('img/'+title+".jpg", "wb") #파이참에서는 img폴더만 적으면 됨 
        f = open('day0422/img/'+title+".jpg", "wb") #vscode에서는 day0422/img라고 상위폴더도 적어줘야함
        f.write(content)
        f.close()
        print(title + "저장됨")
        # print(img_url, title)
print("모두 저장하였습니다.")
# print(len(list))
# print(text)