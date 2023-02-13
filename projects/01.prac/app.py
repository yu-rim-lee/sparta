from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

'''
# Get 방식
@app.route('/test', methods=['GET']) # 1. '/test'라는 창구로 GET 요청이 들어온다
def test_get():
   title_receive = request.args.get('title_give') # 2. 그떄 'title_give'가 들어오면 해당 데이터를 title_receive 변수에 넣는다.
   print(title_receive) # 3. 터미널에 'None'이 찍힌다.
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'}) # 4. 백엔드에서 프론트엔드로 데이터를 내려준다.
'''

# POST 방식
@app.route('/test', methods=['POST']) # 1. '/test'라는 창구로 POST 요청이 들어온다
def test_post():
   title_receive = request.form['title_give'] # 2. 그떄 'title_give'가 들어오면 해당 데이터를 title_receive 변수에 넣는다.
   print(title_receive) # 3. 터미널에 '블랙팬서'가 찍힌다.
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'}) # 4. 백엔드에서 프론트엔드로 데이터를 내려준다.


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)