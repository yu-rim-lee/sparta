from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mmgalfj.mongodb.net/?retryWrites=true&w=majority') # 라이브러리 부르기
db = client.dbsparta

# 퀴즈 1: 영화 제목 '가버나움'의 평점 가져오기
'''
movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])
'''

# 퀴즈 2: '가버나움'의 평점과 같은 평점의 영화 제목들을 가져오기
# 방법 1
'''
all_movies = list(db.movies.find({}, {'_id': False}))
movie = db.movies.find_one({'title':'가버나움'})
for i in all_movies:
    if movie['star'] == i['star']:
        print(i['title'])
'''
# 방법 2
'''
movie = db.movies.find_one({'title':'가버나움'})
target_star = movie['star']
movies = list(db.movies.find({'star':target_star}, {'_id': False}))
for i in movies:
    print(i['title'])
'''

# 퀴즈 3: '가버나움' 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':0}}) 