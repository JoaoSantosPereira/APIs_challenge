from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

#GET
@app.route('/ping', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Responde com pong',
            'examples': {
                'application/json': {'message': 'pong'}
            }
        }
    }
})
def ping():
    return jsonify({'message': 'pong'})

#POST
@app.route('/echo', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'text': {'type': 'string'}
                },
                'required': ['text']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Retorna o texto recebido',
            'examples': {
                'application/json': {'text': 'hello'}
            }
        }
    }
})
def echo():
    data = request.get_json()
    return jsonify({'text': data['text']})