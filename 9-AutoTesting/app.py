from flask import Flask, request, jsonify
from tasks import get_all_tasks, add_task

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"}), 200

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_all_tasks()), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    success, result = add_task(data)
    if success:
        return jsonify(result), 201
    else:
        return jsonify({"error": result}), 400

if __name__ == "__main__":
    app.run(debug=True)