from flask import Flask, request, jsonify, make_response, render_template, send_file
import os
import json

from Json_Parser import parser as give_me_one_bb
from bundle_generation import Bundle, create_bundle_raw, percent_off, project_to_bundle 
from get_all_interets_for_all_users import parser as give_me_all_bb
from get_all_interests_for_user import parser as give_me_all_intrests_bb

import random

def random_time_string():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{hour:02d} : {minute:02d} : {second:02d}"

def format_money(num):
    return f'${num:.2f}'

def sum_money(s1, s2, s3):
    # Remove the dollar sign from each string and convert to a float
    f1 = float(s1[1:])
    f2 = float(s2[1:])
    f3 = float(s3[1:])

    # Add up the three floats
    total = f1 + f2 + f3

    # Format the total as a string with two decimal places and a dollar sign
    return f"${total:.2f}"
app = Flask(__name__)

@app.route('/devtool')
def all_users():

    messages = ""

    if request.method == 'GET':

        data = give_me_all_bb()


        messages = render_template('index.html', data = data)

    resp = make_response(messages, 200)

    if request.method == 'GET':
        resp.headers['Content-Type'] = 'text/html'

    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization'
    
    return resp

@app.route('/devtool/<user_name>')
def all_interests(user_name):

    data = {}
    data["data"] = give_me_all_intrests_bb(user_name)
    data["user"] = user_name

    return render_template('UserName.html', data = data)
    

@app.route('/devtool/<user_name>/<interest>')
def user_bundle(user_name,interest):
    interest_tmp = give_me_one_bb(user_name)

    ten_off = percent_off(0.1)
    products = Bundle(project_to_bundle(create_bundle_raw(interest_tmp)), ten_off)

    while len(products.products) < 3:
        interest_tmp = give_me_one_bb(user_name)

        ten_off = percent_off(0.1)
        products = Bundle(project_to_bundle(create_bundle_raw(interest_tmp)), ten_off)

    print(products.products)

    val_1 = products.products[0]
    val_1 = {
        "name": val_1.name,
        "OG": format_money(val_1.price),
        "new": format_money(val_1.discounted_price()),
        "url": val_1.url,
        "img": val_1.image 
    }

    val_2 = products.products[1]
    val_2 = {
        "name": val_2.name,
        "OG": format_money(val_2.price),
        "new": format_money(val_2.discounted_price()),
        "url": val_2.url,
        "img": val_2.image 
    }

    val_3 = products.products[2]
    val_3 = {
        "name": val_3.name,
        "OG": format_money(val_3.price),
        "new": format_money(val_3.discounted_price()),
        "url": val_3.url,
        "img": val_3.image 
    }

    data = {
        "val_1": val_1,
        "val_2": val_2,
        "val_3": val_3,
        "OG": sum_money(val_1["OG"], val_2["OG"], val_3["OG"]),
        "new": sum_money(val_1["new"], val_2["new"], val_3["new"]),
        "expiry_date": random_time_string(),
        "user": user_name,
        "interest": interest
    }

    return render_template('Intrest.html', data = data)

@app.route('/ext', methods=['GET', 'OPTIONS'])
def user_bundle_data():

    messages = ""

    if request.method == 'GET':
        name = "Wilkinson Delacruz"

        interest = give_me_one_bb(name)

        ten_off = percent_off(0.1)
        products = Bundle(project_to_bundle(create_bundle_raw(interest)), ten_off)

        while len(products.products) < 3:
            interest = give_me_one_bb(name)

            ten_off = percent_off(0.1)
            products = Bundle(project_to_bundle(create_bundle_raw(interest)), ten_off)

        print(products.products)

        val_1 = products.products[0]
        val_1 = {
            "name": val_1.name,
            "OG": format_money(val_1.price),
            "new": format_money(val_1.discounted_price()),
            "url": val_1.url,
            "img": val_1.image 
        }

        val_2 = products.products[1]
        val_2 = {
            "name": val_2.name,
            "OG": format_money(val_2.price),
            "new": format_money(val_2.discounted_price()),
            "url": val_2.url,
            "img": val_2.image 
        }

        val_3 = products.products[2]
        val_3 = {
            "name": val_3.name,
            "OG": format_money(val_3.price),
            "new": format_money(val_3.discounted_price()),
            "url": val_3.url,
            "img": val_3.image 
        }

        data = {
            "val_1": val_1,
            "val_2": val_2,
            "val_3": val_3,
            "OG": sum_money(val_1["OG"], val_2["OG"], val_3["OG"]),
            "new": sum_money(val_1["new"], val_2["new"], val_3["new"]),
            "expiry_date": random_time_string()
        }

        messages = render_template('ext.html', data = data)

    resp = make_response(messages, 200)

    if request.method == 'GET':
        resp.headers['Content-Type'] = 'text/html'

    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization'
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)
