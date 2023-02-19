# API (클라이언트 서버 통신)
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 망고DB 연결
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mmgalfj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    # 데이터 넘겨받음
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    # 넘겨받은 데이터 입력
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)
    
    # 클라이언트로 넘겨줌
    return jsonify({'msg':'저장 완료!'})

@app.route("/mars", methods=["GET"])
def mars_get():
    # 데이터 전체 조회
    mars_data = list(db.mars.find({}, {'_id': False}))
    
    return jsonify({'result' : mars_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)