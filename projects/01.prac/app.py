from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET']) # 1. '/test'라는 창구로 GET 요청이 들어온다
def test_get():
   title_receive = request.args.get('title_give') # 2. 그떄 'title_give'라는 데이터가 있으면 들고 온다
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'}) # 백엔드에서 프론트엔드 데이터 내려주기

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)