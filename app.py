from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbStocks


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/post', methods=['POST'])
def save_order():
    receive_choice = 'men'

    return jsonify({'msg': '주문이 완료되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/post', methods=['GET'])
def view_orders():


    return jsonify({'msg': '주문이 완료되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
