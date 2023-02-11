import certifi
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.ynnqkbk.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.bread

app = Flask(__name__)
@app.route('/create' , methods=["POST"])
def save_create():
    title_receive = request.form['title_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_give']
    number_receive = request.form['number_give']
    best_receive = request.form['best_give']
    day_receive = request.form['day_give']
    x_receive = request.form['x_give']
    y_receive = request.form['y_give']
    # image_receive = request.files['image_give']

    doc = {
        'title': title_receive,
        'address': address_receive,
        'star': star_receive,
        'number': number_receive,
        'best': best_receive,
        'day': day_receive,
        'x': x_receive,
        'y': y_receive,
        # 'image': image_receive,

    }
    db.breads.insert_one(doc)

    return jsonify({'msg': '추천 빵집 생성'})


# 메인페이지!!
@app.route('/showmain', methods=['GET'])
def showmain():
    all_bread = list(db.breads.find({},{'_id':False}))
    return jsonify({'msg': all_bread})


# 상세페이지 이동!
@app.route('/<int:articles_pk>')
def create(articles_pk):
    title = db.breads.find_one({'articles_pk':'articles_pk'})['title']
    address = db.breads.find_one({'articles_pk':'articles_pk'})['address']
    star = db.breads.find_one({'articles_pk':'articles_pk'})['star']
    number = db.breads.find_one({'articles_pk':'articles_pk'})['number']
    day = db.breads.find_one({'articles_pk':'articles_pk'})['day']
    image = db.breads.find_one({'articles_pk':'articles_pk'})['image']
    articles_pk = db.breads.find_one({'articles_pk':'articles_pk'})['articles_pk']
    return render_template('create.html', title=title, address=address, star=star, number=number, day=day,image=image, articles_pk=articles_pk)


# 글작성 페이지 이동
@app.route('/create')
def create():
    return render_template('create.html')


# 로그인 페이지 이동
@app.route('/login')
def login():
    return render_template('login.html')


# 회원가입 페이지 이동
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

