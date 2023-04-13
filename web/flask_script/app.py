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

    room_members = db.data_getter("""
    SELECT room_id, user_id, ip_address
    FROM room_member
    WHERE room_id = %(room_id)s;
    """,
    {'room_id': room_id})

    user_id = -1
    status = True

    for row in room_members:
        _room_id, _user_id, _ip_address  = row
        if ip_address == _ip_address:
            user_id = _user_id

    if user_id == -1:
        user_id = len(room_members)
        status = db.data_inserter("""
        INSERT INTO room_member(room_id, user_id, ip_address)
        VALUES (%(room_id)s, %(ip_address)s, %(user_id)s);
        """,
        {'room_id': room_id, 'ip_address': ip_address, 'user_id': user_id})

    if status == False:
        user_id = -1

    return jsonify({
        'status': status,
        'room_id': room_id,
        'ip_address': ip_address,
        'user_id': user_id,
        'isSuperUser': (user_id == 0)
    })

@app.route('/image/upload', methods=['POST'])
def upload_image():
    room_id = request.json.get('room_id')
    prompt = request.json.get('prompt')
    image_base64 = request.json.get('image')
    # TODO: image
    return jsonify({
        'room_id': room_id,
        'prompt': prompt,
        'todo': 'same image in a path'
    })

@app.route('/image/get', methods=['GET'])
def get_image():
    room_id = request.json.get('room_id')

    sql = """
    SELECT room_id, prompt, updated_at
    FROM image
    WHERE room_id = %(room_id)s;
    """
    data = {'room_id': room_id}
    image_info = db.data_getter(sql, data)

    prompt = ""
    updated_at
    if(len(image_info) == 1):
        _, prompt, updated_at = image_info[0] # data is only one line

    return jsonify({
        'room_id': room_id,
        'image': 'todo, url',
        'prompt': prompt,
        'updated_at': updated_at,
        'todo': 'get newest image'
    })

@app.route('/chat/send', methods=['POST'])
def send_message():
    room_id = request.json.get('room_id')
    user_id = request.json.get('user_id')
    message = request.json.get('message')
    sql = """
    INSERT INTO chat(room_id, user_id, message)
    VALUES (%(room_id)s, %(user_id)s, %(message)s);
    """
    data = {'room_id': room_id, 'user_id': user_id, 'message': message}
    return jsonify({
        'status': db.data_inserter(sql, data)
    })

@app.route('/chat/history', methods=['GET'])
def get_message_history():
    room_id = request.args.get('room_id')

    sql = """
    SELECT user_id, message, created_at
    FROM chat
    WHERE room_id = %(room_id)s
    ORDER BY created_at DESC
    LIMIT 7;
    """
    data = {'room_id': room_id}

    rows = db.data_getter(sql, data)

    chat_history = []
    for row in rows:
        _user_id, _message, _created_at = row
        chat_history.append({
            'user_id': _user_id,
            'message': _message,
            'created_at': _created_at
        })

    return jsonify({
        'chat_history': chat_history,
        'latest_date': rows[0][2]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)