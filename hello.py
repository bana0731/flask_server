from flask import Flask, escape, request, render_template
import random
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/myname')
def myname():
    return '한상이입니다.'

# 랜덤으로 점심 메뉴 추천해주는 서버
@app.route('/lunch')
def lunch():
    menus = ['김밥','20층','빠바','짜장면','똠얌꿍','수제비','돈가스']
    lunch = random.choice(menus)
    return lunch

# 아이돌 백과사전
@app.route('/idol')
def idol():
    idols = {
        'b1a4':{
            '진영':29,
            '신우':29,
            '산들':28,
            '바로':28,
            '공찬':27
        },
        'rv':['웬디','아이린','슬기','조이','예리'],
        'onf':'온앤오프',
        'omg':'오마이걸'
    }
    return idols

@app.route('/post/<int:num>')
def post(num):
    posts = ['0번 포스트','1번포스트','2번포스트']
    return posts[num]


#실습 큐브뒤에 전달된 수의 세제곱수를 화면에 보여주세요.
# 1->1
#2-> 8
#3->27
#str() : 숫자를 문자로 바꿔주는 함수.
@app.route('/cube/<int:num>')
def cube(num):
    cubed = num*num*num
    return str(cubed)

# 클라이언트에게 html 파일을 주고싶어요.
@app.route('/html')
def html():
    return render_template('hello.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    #age = request.args{'age']
    return render_template('pong.html',age_in_html=age)

# 로또 번호를 가져와서 보여주는 서버만들기
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests(url).json()

    winner = []
    for i in range(1,7):
        winner.append(result.get(f'drwtNo{i}'))
        #winner.append(result[f'drwtNo{i}'])    
     winner.append(result.get('bnusNo'))
    return json.dumps(winner)



app.run(debug=True)