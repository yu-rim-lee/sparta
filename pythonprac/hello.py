import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 전체 html 가져오는 것을 확인할 수 있다.
# print(soup)


a = soup.select_one('#old_content > table > tbody > tr:nth-child(3) > td.title > div > a')

# 지정된 html 부분만 가져오는 것을 확인할 수 있다. (솎아냄)
# print(a)

# 속성 값 가져오기(bs4 - 꺽새)
# print(a['href'])

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(3)
trs = soup.select('#old_content > table > tbody > tr') # tr 공통 -> tr들이 리스트로 쌓인다.
for tr in trs:
    #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
    a = tr.select_one('td.title > div > a') # 영화 제목
    print(a)

    # 구분선이 None으로 표시됨을 방지
    if a is not None:
        print(a.text)