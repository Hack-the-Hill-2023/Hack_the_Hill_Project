from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

@app.route('/devtool')
def all_users():
    return f'dev tools'

@app.route('/devtool/<user_name>')
def all_interests(user_name):
    return f'{user_name}`s interests'

@app.route('/devtool/<user_name>/<interest>')
def user_bundle(user_name,interest):
    return f'{user_name}: {interest}'

@app.route('/ext', methods=['GET', 'OPTIONS'])
def user_bundle_data():

    messages = {}

    if request.method == 'GET':
        messages["data"] = "Hello world"

    resp = make_response(jsonify(messages), 200)

    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization'
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)