from pymongo import MongoClient
import certifi
import sys
import json
from flask import Flask, render_template, request, jsonify
import bcrypt as bcrypt

# 이 코드 지우지말아주세요!!
ca = certifi.where()

# client = MongoClient(
#     'mongodb+srv://test:sparta@cluster0.oj62xnf.mongodb.net/?retryWrites=true&w=majority')
# db = client.bread


client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.ynnqkbk.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbsparta
app = Flask(__name__)


@ app.route('/')
def home():
    return render_template('index.html')


@ app.route('/index2')
def home2():
    return render_template('index2.html')


@ app.route('/detail')
def detail():
    return render_template('detail.html')

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
    contents_list = list(db.breadcontents.find({}, {'_id': False}))
    return jsonify({'contents': contents_list})


# 글작성 페이지
@ app.route('/create', methods=["POST"])
def save_create():
    print(request.form.get('title_give'))
    title_receive = request.form.get('title_give')
    address_receive = request.form.get('address_give')
    star_receive = request.form.get('star_give')
    number_receive = request.form.get('number_give')
    best_receive = request.form.get('best_give')
    day_receive = request.form.get('day_give')
    x_receive = request.form.get('x_give')
    y_receive = request.form.get('y_give')
    image_receive = request.form.get('image_give')
    print(title_receive)
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
        return jsonify({'msg': '추천 빵집 생성'})
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


# 수정완료
@app.route('/update', methods=['PUT'])
def update():
    title_receive = request.form.get('title_give')
    address_receive = request.form.get('address_give')
    star_receive = request.form.get('star_give')
    number_receive = request.form.get('number_give')
    best_receive = request.form.get('best_give')
    day_receive = request.form.get('day_give')
    x_receive = request.form.get('x_give')
    y_receive = request.form.get('y_give')
    image_receive = request.form.get('image_give')
    articles_pk = request.form.get('articles_pk_give')
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

    db.breads.update_one({'articles_pk': articles_pk}, {'$set': doc})

    return jsonify({'msg': '수정완료!'})

# 글작성 페이지 이동


@app.route('/create')
def create():

    return render_template('create.html')

# 메인페이지1


@app.route('/showmain', methods=['GET'])
def showmain():
    all_bread = list(db.breads.find({}, {'_id': False}))
    return jsonify({'msg': all_bread})

# 메인페이지2


@app.route('/showmain2', methods=['GET'])
def showmain2():
    all_bread = list(db.breads.find({}, {'_id': False}))
    return jsonify({'msg': all_bread})

# 상세페이지 이동


@app.route('/detail/<int:articles_pk>')
def detailpage(articles_pk):
    target = db.breads.find_one({'articles_pk': articles_pk})
    title = target['title']  # 상호명
    address = target['address']  # 주소
    star = target['star']  # 평점
    number = target['number']  # 전화번호
    day = target['day']  # 휴무일
    image = target['image']  # 이미지
    best = target['best']  # 베스트빵
    x = target['x']  # 베스트빵
    y = target['y']  # 베스트빵
    articles_pk = target['articles_pk']  # 고유번호
    return render_template('detail.html', best=best, title=title, address=address, star=star, number=number, day=day, image=image, articles_pk=articles_pk, x=x, y=y)

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
@app.route('/updatepage/<int:articles_pk>')
def updatepage(articles_pk):

    target = db.breads.find_one({'articles_pk': articles_pk})
    title = target['title']  # 상호명
    address = target['address']  # 주소
    star = target['star']  # 평점
    number = target['number']  # 전화번호
    day = target['day']  # 휴무일
    image = target['image']  # 이미지
    best = target['best']  # 베스트빵
    x = target['x']  # 베스트빵
    y = target['y']  # 베스트빵
    articles_pk = target['articles_pk']  # 고유번호
    return render_template('update.html', title=title, address=address, star=star, number=number, day=day, image=image, articles_pk=articles_pk, best=best, x=x, y=y)

# 빵삭제


@app.route("/detail/delete", methods=["POST"])
def detail_delete():
    deletepk_receive = request.form["deletepk_give"]
    db.breads.delete_one({'articles_pk': int(deletepk_receive)})
    return jsonify({'msg': '삭제완료!'})


# 채크코드
@app.route('/signup/check', methods=["GET"])
def signUpGet():
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'users': userList})


@app.route('/signup/give', methods=["POST"])
def signUpPost():
    id_receive = request.form["id_give"]
    name_receive = request.form["name_give"]
    pw_receive = request.form["pw_give"]

    hashedPassword = bcrypt.hashpw(
        pw_receive.encode('utf-8'), bcrypt.gensalt())
    hashedPassword = hashedPassword.decode()

    doc = {
        'id': id_receive,
        'name': name_receive,
        'pw': hashedPassword
    }
    db.users.insert_one(doc)
    return jsonify({'msg': '가입완료!'})

@app.route('/signin/give', methods=["POST"])
def signInGive():
    id_receive = request.form["id_give"]
    pw_receive = request.form["pw_give"]

    user = list(db.users.find({'id': id_receive}, {'_id': False}))
    if len(user) > 0 and bcrypt.checkpw(pw_receive.encode('utf-8'), user[0]['pw'].encode('utf-8')):
        doc = {
            'userid': user[0]['id'],
            'username': user[0]['name']
        }
        return jsonify({'error': None, 'data': doc})
    else:
        return jsonify({'error': 'login-fail'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
