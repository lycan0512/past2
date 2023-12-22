from dbdb import insert_data
from flask import Flask, render_template, request
import dbdb # 내가 만든 데이터베이스 함수들

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<body>
<h1>웹앱프로그래밍</h1>
<p><a href="http://127.0.0.1:5000/hello">헬로우 페이지</a></p>
<p><a href="http://127.0.0.1:5000/naver">네이버 페이지</a></p>
<p><a href="http://127.0.0.1:5000/singin">가입 페이지</a></p>
<p><a href="http://127.0.0.1:5000/login">로그인 페이지</a></p>
</body>
</html>
'''

@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
     return "데이터를 받아주는 페이지"
    else:
     #여기 POST로 들어오는 데이터를 받아보자
     search =  request.form['fname']
     print("전달된값:",search)
     return "당신이 검색한 키워드(POST)<br>{}입니다".format(search)

@app.route('/singin')
def singin():
    return render_template("singin.html")

@app.route('/action_page', methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
     return "데이터를 받아주는 페이지"
    else:
     #여기 POST로 들어오는 데이터를 받아보자
     email =  request.form['email']
     password =  request.form['password']
     print("전달된값:",email, password)
     insert_data(email,password)
     return "회원가입 데이터(POST)"



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
     
    else:
     #여기 POST로 들어오는 데이터를 받아보자
      email =  request.form['email']
      password =  request.form['password']
      print("전달된값:",email, password)
      if email ==  'a@a.com' and password == '1234':
       return("로그인 성공")
      else:
       print("아이디 패스워드 확인")
       return "로그인 데이터(POST)"


if __name__ == '__main__':
    app.run()
