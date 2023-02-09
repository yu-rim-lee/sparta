from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mmgalfj.mongodb.net/?retryWrites=true&w=majority') # 라이브러리 부르기
db = client.dbsparta

# 몽고DB는 딕셔너리를 넣어주면 된다 
doc = {
    'name':'영수',
       'age':24
}

# 'users' 라는 명칭의 collection이다.
db.users.insert_one(doc)