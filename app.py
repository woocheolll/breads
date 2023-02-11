from pymongo import MongoClient
import certifi
import sys
import json
from flask import Flask, render_template, request, jsonify

# client = MongoClient(
#     'mongodb+srv://test:sparta@cluster0.oj62xnf.mongodb.net/?retryWrites=true&w=majority')
# db = client.bread

client = MongoClient(
    'mongodb+srv://test:as123123@cluster0.nnsglfi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)


@ app.route('/')
def home():
    return render_template('index.html')


@ app.route('/detail/<articles_pk>')
def detail():
    return render_template('detail.html',articles_pk=articles_pk)

# 로그인 페이지 이동


@app.route('/signin')
def login():
    return render_template('signin.html')


# 회원가입 페이지 이동
@app.route('/signup')
def signup():
    return render_template('signup.html')


@ app.route("/showdetail", methods=["GET"])
def contents_get():
    contents_list = list(db.breads.find({}, {'_id': False}))
    return jsonify({'contents': contents_list})


# 글작성 페이지
@ app.route('/create', methods=["POST"])
def save_create():
    title_receive = request.form['title_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    number_receive = request.form['number_give']
    best_receive = request.form['best_give']
    day_receive = request.form['day_give']
    x_receive = request.form['x_give']
    y_receive = request.form['y_give']
    image_receive = request.form['image_give']

    count = list(db.breads.find({}, {'_id': False}))

    if count == []:
        articles_pk = 1
        doc = {
            'articles_pk': articles_pk,
            'title': title_receive,
            'address': address_receive,
            'star': star_receive,
            'number': number_receive,
            'best': best_receive,
            'day': day_receive,
            'x': x_receive,
            'y': y_receive,
            'image': image_receive,

        }
        db.breads.insert_one(doc)
    else:
        num1 = count[len(count)-1]
        num = num1['articles_pk']
        articles_pk = num + 1
        doc = {
            'articles_pk': articles_pk,
            'title': title_receive,
            'address': address_receive,
            'star': star_receive,
            'number': number_receive,
            'best': best_receive,
            'day': day_receive,
            'x': x_receive,
            'y': y_receive,
            'image': image_receive,

        }
        db.breads.insert_one(doc)

    return jsonify({'msg': '추천 빵집 생성'})


@app.route('/create', methods=['PUT'])
def update():
    title_receive = request.form['title_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    number_receive = request.form['number_give']
    best_receive = request.form['best_give']
    day_receive = request.form['day_give']
    x_receive = request.form['x_give']
    y_receive = request.form['y_give']
    image_receive = request.form['image_give']
    articles_pk = request.form['articles_pk']
    doc = {
        'articles_pk':articles_pk,
        'title': title_receive,
        'address': address_receive,
        'star': star_receive,
        'number': number_receive,
        'best': best_receive,
        'day': day_receive,
        'x': x_receive,
        'y': y_receive,
        'image': image_receive,
    }
    db.breads.update_one({'articles_pk':'articles_pk'},{'$set':doc})

# 글작성 페이지 이동


@app.route('/create')
def create():

    return render_template('create.html')

# 메인페이지


@app.route('/showmain', methods=['GET'])
def showmain():
    all_bread = list(db.breads.find({}, {'_id': False}))
    return jsonify({'msg': all_bread})


# 상세페이지 이동
@app.route('/detail/<int:articles_pk>')
def detailpage(articles_pk):
    title = db.breads.find_one({'articles_pk': articles_pk})['title']
    address = db.breads.find_one({'articles_pk': articles_pk})['address']
    star = db.breads.find_one({'articles_pk': articles_pk})['star']
    number = db.breads.find_one({'articles_pk': articles_pk})['number']
    day = db.breads.find_one({'articles_pk': articles_pk})['day']
    image = db.breads.find_one({'articles_pk': articles_pk})['image']
    best = db.breads.find_one({'articles_pk': articles_pk})['best']
    articles_pk = db.breads.find_one(
        {'articles_pk':articles_pk})['articles_pk']
    return render_template('detail.html',best=best, title=title, address=address, star=star, number=number, day=day, image=image, articles_pk=articles_pk)

# 댓글


@app.route("/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']

    count = list(db.comment.find({}, {'_id': False}))
    num = len(count) + 1

    doc = {
        'num': num,
        'comment': comment_receive,
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '작성 완료!'})


@app.route("/comment/delete", methods=["POST"])
def comment_delete():
    num_receive = request.form["num_give"]
    db.comment.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제!'})


@app.route("/comment", methods=["GET"])
def comment_get():
    comments_list = list(db.comment.find({}, {'_id': False}))
    print(comments_list)
    return jsonify({'comments': comments_list[::-1]})


# 수정페이지 이동
@app.route('/<int:articles_pk>/update')
def updatepage(articles_pk):
    title = db.breads.find_one({'articles_pk': articles_pk})['title'] # 상호명
    address = db.breads.find_one({'articles_pk': articles_pk})['address'] #주소
    star = db.breads.find_one({'articles_pk': articles_pk})['star'] #평점
    number = db.breads.find_one({'articles_pk': articles_pk})['number'] # 전화번호
    day = db.breads.find_one({'articles_pk': articles_pk})['day'] #휴무일
    image = db.breads.find_one({'articles_pk': articles_pk})['image'] # 이미지
    best = db.breads.find_one({'articles_pk': articles_pk})['best'] # 베스트빵
    articles_pk = db.breads.find_one(
        {'articles_pk': articles_pk})['articles_pk'] # 고유번호
    return render_template('detail.html', title=title, address=address, star=star, number=number, day=day, image=image, articles_pk=articles_pk, best=best)

#빵삭제
@app.route("/detail/delete", methods=["POST"])
def detail_delete():
    deletepk_receive = request.form["deletepk_give"]
    db.breads.delete_one({'articles_pk': int(deletepk_receive)})
    return jsonify({'msg': '삭재완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
