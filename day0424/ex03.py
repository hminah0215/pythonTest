from bs4 import BeautifulSoup

# 34 페이지

html = '''
    <html>
        <body>
            <h1 id='title'>스크레이핑이란?</h1>
            <p id='body'>웹페이지를 분석하는 것</p>
            <p>원하는 부분을 추출하는 것</p>
        </body>
    </html>
    '''

soup = BeautifulSoup(html,'html.parser')

title = soup.find(id='title')
print(title.string)
body = soup.find(id='body')
print(body.string)