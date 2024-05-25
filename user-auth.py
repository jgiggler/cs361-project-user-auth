from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

def hash_password(password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    return hashed_pw

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    hashed_pw = hash_password(password)
    with open('logins.txt', 'r') as users:
        for line in users:
            
            user_data = json.loads(line)

            if username in user_data and user_data[username]['password'] == hashed_pw:
                print("User Found")
                users.close()
                return jsonify({'message': 'Login successful'}), 200
        users.close()
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    hashed_pw = hash_password(password)
    email = data.get('email')
    # check if username is already in use on users list
    with open('logins.txt', 'r') as users:
        for line in users:
            
            user_data = json.loads(line)
            
            if username in user_data:
                print("username found")
                return jsonify({'message': 'Username already in use'})
    users.close()

    # add username to users list
    with open('logins.txt', 'a') as users:        
        user = {username: {'password': hashed_pw, 'email': email}}
        print(user)
        user_string = json.dumps(user)
        users.write(user_string+'\n')
        users.close()
        return jsonify({'message': 'Success'})
    

if __name__ == '__main__':
    app.run(debug=True)
                    
