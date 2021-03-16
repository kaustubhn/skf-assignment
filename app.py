from flask import Flask
import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

app = Flask(__name__)

@app.route('/publish', methods=['POST'])
def publish():
    return 'Hello, World!'

@app.route('/getLast', methods=['GET'])
def get_last():
    return 'Hello, World!'

@app.route('/getByTime', methods=['GET'])
def get_by_time():
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(host="0.0.0.0")