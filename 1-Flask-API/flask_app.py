from flask import Flask,jsonify,request

app = Flask(__name__)

# GET /ping
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200


# POST /echo
@app.route('/echo', methods=['POST'])
def echo():

    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Mandatory 'text' field!"}), 400
    
    return jsonify({"text": data['text']}), 200

if __name__ == '__main__':
    app.run(debug=True)
