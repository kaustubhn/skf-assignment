import redis, time
from flask import Flask, request, jsonify
from flask import make_response, abort
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_USE_SSL, REDIS_SSL_CERT
from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG


try:
    print('Trying to connect to Redis')
    r = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        decode_responses=True
    )
    print('Successfully connected to Redis server')
except Exception as e:
    print("Error: Unable to connect to redis.")
    print(e)
    

app = Flask(__name__)

# Error handling
@app.errorhandler(400)
def invalid_body(error):
    return make_response(jsonify({'error': 'Invalid request body'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 405)

@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


# Routes
@app.route('/api/v1/publish', methods=['POST'])
def publish():
    if request.method == 'POST':
        if not request.json or not 'content' in request.json:
            abort(400)
        else:
            try:
                r.zadd('contents', {request.json["content"]: round(time.time()*1000)})
                return make_response(jsonify({"status": "success"}), 200)
            except Exception as e:
                print(e)
                abort(500)
    else:
        abort(405)

@app.route('/api/v1/getLast', methods=['GET'])
def get_last():
    if request.method == 'GET':
        return make_response(jsonify({"content": r.zrange('contents', -1, -1)[0]}), 200)
    else:
        abort(405)

@app.route('/api/v1/getByTime', methods=['POST'])
def get_by_time():
    if request.method == 'POST':
        if not request.json or not 'start' in request.json or not 'end' in request.json:
            abort(400)
        else:
            try:
                print(request.json['start'])
                print(request.json['end'])
                return make_response(jsonify({"content": r.zrange('contents', request.json['start'], request.json['end'])}), 200)
            except Exception as e:
                print(e)
                abort(500)
    else:
        abort(405)

if __name__ == '__main__':
   app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
   