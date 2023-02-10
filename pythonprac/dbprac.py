from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mmgalfj.mongodb.net/?retryWrites=true&w=majority') # 라이브러리 부르기
db = client.dbsparta


# insert 한 개 입력
doc = {'name':'영수','age':24} # 몽고DB는 딕셔너리를 넣어주면 된다 
db.users.insert_one(doc) # 'users' 라는 명칭의 collection이다.


# select 전체 조회 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({}, {'_id': False})) # {} 조건 없음, {'_id': False} '_id' 값 제거
for i in all_users:
    print(i)

    
# select 한 개 조회 ( _id 값은 제외하고 출력)
user = db.users.find_one({}, {'_id': False})
user = db.users.find_one({'name':'철수'})
print(user)


# update 한 개 갱신
db.users.update_one({'name':'영수'},{'$set':{'age':19}}) # name이 영수인 것을 찾아서 age을 19로 바꿔라


# delete 한 개 삭제
db.users.delete_one({'name':'영수'})
