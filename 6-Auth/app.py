from flask import Flask, jsonify, request
from functools import wraps
# Assume Valid token as secrettoken123

app = Flask(__name__)

@app.before_request

def check_auth():
    # Lista de rotas que não precisam de autenticação
    open_endpoints = ['/ping', '/docs']
    
    if request.path in open_endpoints:
        return  # Não exige token

    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid Authorization header'}), 401 # Unauthorized
    token = auth_header.split(' ')[1]
    if token != 'secrettoken123':
        return jsonify({'error': 'Unauthorized'}), 401 # Unauthorized

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing or invalid Authorization header'}), 401
        token = auth_header.split(' ')[1]
        if token != "secrettoken123":
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return wrapper

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/secret')
@require_auth
def secret():
    return jsonify({'message': 'You are authenticated!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)