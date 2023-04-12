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

@app.route('/room/info', methods=['GET'])
def get_room_info():
    room_id = request.args.get('room_id')
    ip_address = request.args.get('ip_address')
    sql = """
    SELECT
        room_id,
        user_id,
        ip_address,
        created_at
    FROM
        room_member
    WHERE room_id = '{}';
    """.format(room_id)

    room_members = db.data_getter(sql)
    print(room_members)

    return jsonify({
        'room_id': room_id,
        'ip_address': ip_address,
        'todo': 'get username, and whether user is superuser'
    })

@app.route('/image/upload', methods=['POST'])
def upload_image():
    room_id = request.json.get('room_id')
    prompt = request.json.get('prompt')
    # TODO: image
    return jsonify({
        'room_id': room_id,
        'prompt': prompt,
        'todo': 'same image in a path'
    })

@app.route('/image/get', methods=['GET'])
def get_image():
    room_id = request.json.get('room_id')
    return jsonify({
        'room_id': room_id,
        'todo': 'get newest image'
    })

@app.route('/chat/send', methods=['POST'])
def send_message():
    room_id = request.json.get('room_id')
    ip_address = request.json.get('ip_address')
    message = request.json.get('message')
    return jsonify({
        'room_id': room_id,
        'ip_address': ip_address,
        'message': message,
        'todo': 'receive message and update to database'
    })

@app.route('/chat/history', methods=['GET'])
def get_message_history():
    room_id = request.args.get('room_id')
    return jsonify({
        'room_id': room_id,
        'todo': 'get chat history'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)