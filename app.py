from flask import Flask, request, jsonify
from flask import make_response, abort
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_USE_SSL, REDIS_SSL_CERT
from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG
import redis

try:
    print('Trying to connect to Redis')
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB
    )
    print('Successfully connected to Redis server')
except Exception as e:
    print("Error: Unable to connect to redis.")
    print(e)
    

app = Flask(__name__)


# Error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def invalid_body(error):
    return make_response(jsonify({'error': 'Invalid request body'}), 400)


# Routes
@app.route('/api/v1/publish', methods=['POST'])
def publish():
    if request.method == 'POST':
        if not request.json or not 'content' in request.json:
            abort(400)
        else:
            try:
                r.set("content",request.json["content"])
                return make_response(jsonify({"status": "success"}), 200)
            except Exception as e:
                print(e)
                return make_response(jsonify({"status": "error"}), 500)
    else:
        return jsonify({"error": "Invalid Method"})

@app.route('/api/v1/getLast', methods=['GET'])
def get_last():
    if request.method == 'GET':
        return make_response(jsonify({"content": r.get('content')}, 200))
    else:
        return jsonify({"error": "Invalid Method"})

@app.route('/api/v1/getByTime', methods=['GET'])
def get_by_time():
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
   