from flask import Flask, request, jsonify, redirect, url_for, flash

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'my_key'

users = {
    'user1': {'password': 'password1'},

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



if __name__ == '__main__':
    app.run(debug=True)
                    
