# mongoDB 연결
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mmgalfj.mongodb.net/?retryWrites=true&w=majority') # 라이브러리 부르기
db = client.dbsparta


# 웹 크롤링에 필요한 라이브러리
import requests
from bs4 import BeautifulSoup


# 웹 크롤링 준비
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


# <tr>
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2)
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    # <a> 순위
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
    rank = tr.select_one('td.number').text[0:2].strip()

    # <a> 곡제목
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()

    # <a> 가수
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.artist.ellipsis
    artist = tr.select_one('td.info > a.artist.ellipsis').text.strip()

    print(rank, title, artist)