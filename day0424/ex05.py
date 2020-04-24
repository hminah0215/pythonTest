from bs4 import BeautifulSoup
import requests

#elGoldRateInfo > div.box > div > div.present > div > div > p:nth-child(1) > em   ////네이버금시세

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EA%B8%88%EC%8B%9C%EC%84%B8"
text = requests.get(url).text

soup = BeautifulSoup(text, "html.parser")
r = soup.select_one("#elGoldRateInfo > div.box > div > div.present > div > div > p:nth-child(1) > em").string
print(r)
