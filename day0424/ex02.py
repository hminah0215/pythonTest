from bs4 import BeautifulSoup

# 34 페이지

html = '''
    <html>
        <body>
            <h1>스크레이핑이란?</h1>
            <p>웹페이지를 분석하는 것</p>
            <p>원하는 부분을 추출하는 것</p>
        </body>
    </html>
    '''

soup = BeautifulSoup(html,'html.parser')
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
    # .next_sibling을 두번적는이유, p태그가 두줄에 걸쳐 작성되어 있어서 첫번째 p 태그 옆의 공백도 
    # 형제로 인식되기때문! 원하는 두번째 p태그의 내용을 가져오고싶다면 두번 적어줘야함 
# print(h1)
# print(type(h1))
# print(p1.string)
print(p2.string)