import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for
import family_controller
from db import create_tables

app = Flask(__name__)


# Gets all family members in HTML page.
@app.route("/", methods=['GET'])
def home():
    # return "<h2>Welcome to API </h2>" \
    #        "<a href= 'http://127.0.0.1:8000/api'> All family. </a> </br>" \
    #        "<a href= 'http://127.0.0.1:8000/api/<id>'> one family. </a>"
    rows = family_controller.get_all_family()
    print(rows)
    return render_template('index.html', rows=rows)


# Gets one family member.
@app.route("/<id1>", methods=['GET'])
def get_one_family_member_html(id1):
    row = family_controller.get_one_family(id1)
    print(row)
    return render_template("family_member.html", row=row)


@app.route("/add_family_member", methods=['POST'])
def add_one_family_member_html():
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    age = request.form['age']
    result = family_controller.insert_family(f_name, l_name, age)
    return render_template("index.html")


@app.route("/api", methods=['GET'])
def get_all_family():
    fam = family_controller.get_all_family()
    return jsonify(fam)


@app.route("/api/<id1>", methods=['GET'])
def get_one_family_member(id1):
    data = family_controller.get_one_family(id1)
    return jsonify(data)


@app.route("/api", methods=['POST'])
def insert_family_member():
    data = request.get_json()
    f_name = data['f_name']
    l_name = data['l_name']
    age = data['age']
    result = family_controller.insert_family(f_name, l_name, age)
    return jsonify(result)


@app.route("/api", methods=['PUT'])
def update_family_member():
    data = request.get_json()
    id1 = int(data['id'])
    f_name = data['f_name']
    l_name = data['l_name']
    age = int(data['age'])
    # print(id1, f_name, l_name, age)
    result = family_controller.update_family_member(f_name, l_name, age, id1)
    return jsonify(result)


@app.route("/api/<id1>", methods=['DELETE'])
def delete_family_member(id1):
    data = family_controller.delete_family_member(id1)
    return jsonify(data)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
