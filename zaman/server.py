from flask import Flask

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

@app.route('/ext/<user_name>/<interest>')
def user_bundle_data(user_name,interest):
    return f'raw data for: {user_name}: {interest}'

if __name__ == '__main__':
    app.run(debug=True)