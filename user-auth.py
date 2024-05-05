from flask import Flask, request, jsonify, redirect, url_for, flash

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'my_key'

users = {
    'user1': {'password': 'password1', 'email': 'j@g.com'},
    ''     : {'password': '1234', 'email': 'j@g.com'}
    }


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username]['password'] == password:
        return jsonify({'message': 'Login successful'}), 200
    
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if username in users:
        return jsonify({'message': 'Username already in use'})
    if username not in users:
        users[username] = {'password': password, 'email': email}
        print(users)
        return jsonify({'message': 'Success'})

if __name__ == '__main__':
    app.run(debug=True)
                    
