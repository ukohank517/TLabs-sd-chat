from flask import Flask, Blueprint, jsonify, request, Response, render_template

app = Flask(__name__)
@app.route('/', methods=['GET'])
def top():
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)