from flask import Flask, Blueprint, redirect, jsonify, request, Response, render_template
from flask_cors import CORS
import uuid
from MySQL import MySQL


db = MySQL()
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def top():
    return render_template('top.html')

@app.route('/room/new', methods=['GET'])
def create_room():
    room_id = str(uuid.uuid4()).replace('-','')
    return redirect("http://20.210.110.182:7860/" + room_id)

@app.route('/room/info')
def get_room_info():
    return jsonify({
        'todo': 'get username, and whether user is superuser'
    })

@app.route('/chat/send', methods=['POST'])
def send_message():
    return jsonify({
        'todo': 'receive message and update to database'
    })

@app.route('/chat/history', methods=['GET'])
def get_message_history():
    return jsonify({
        'todo': 'get chat history'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)