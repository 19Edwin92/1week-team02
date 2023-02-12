# Flask 서버 사용을 위한 import
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# MongoDB 사용을위한 import pymongo, certifi(Mac에서의 접근을 위한 인코딩)
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient(
    "mongodb+srv://19Edwin92:team02@cluster0.8pa7k6r.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
user_db = client.team02
########################################################################################################################################################################################################
# app.route 작성시 유의사항(아래와 같이 누가 작성했는지를 명시해주세요.)
## 작성자 : 박영찬
## 내용 : 회원가입 페이지 경로

########################################################################################################################################################################################################

## 작성자 : 박영찬
## 내용 : 회원가입 페이지 경로
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)