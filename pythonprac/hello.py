# mongoDB 연결
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mmgalfj.mongodb.net/?retryWrites=true&w=majority') # 라이브러리 부르기
db = client.dbsparta


# 웹 크롤링에 필요한 라이브러리
import requests
from bs4 import BeautifulSoup


# 웹 크롤링 준비
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


trs = soup.select('#old_content > table > tbody > tr') # 영화 리스트 공통 부분

for tr in trs:
    #old_content > table > tbody > tr:nth-child(3) > td.title > div > a
    a = tr.select_one('td.title > div > a') # 영화 제목

    # 구분선 None 제거
    if a is not None:
        title = a.text # 영화 제목
        # print(title)
        
        #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        rank = tr.select_one('td:nth-child(1) > img')['alt'] # 랭킹 이미지[순위]
        # print(rank)

        #old_content > table > tbody > tr:nth-child(2) > td.point
        star = tr.select_one('td.point').text # 영화 평점
        # print(star)

        print(rank, title, star)
        '''
        doc = {'title':title, 'rank':rank, 'star':star}
        db.movies.insert_one(doc)
        '''