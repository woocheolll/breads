from pymongo import MongoClient
import certifi
import sys
import json
from flask import Flask, render_template, request, jsonify

client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.oj62xnf.mongodb.net/?retryWrites=true&w=majority')
db = client.bread

# client = MongoClient(
#     'mongodb+srv://test:as123123@cluster0.nnsglfi.mongodb.net/?retryWrites=true&w=majority')
# db = client.dbsparta
app = Flask(__name__)


@ app.route('/')
def home():
    return render_template('index.html')


@ app.route('/detail')
def detail():
    return render_template('detail.html')


@ app.route("/showdetail", methods=["GET"])
def contents_get():
    contents_list = list(db.breadcontents.find({}, {'_id': False}))
    return jsonify({'contents': contents_list})


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
    image_receive = request.files['image_give']

    doc = {
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


@ app.route('/create')
def create():

    return render_template('create.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
