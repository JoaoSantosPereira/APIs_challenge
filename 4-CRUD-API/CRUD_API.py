from flask import Flask, jsonify, request, abort

app = Flask("__main__") 

# mock data
tasks = [
    {"id": 1, "title": "Creating CRUD API","done": False},
    {"id": 2, "title": "Estudar Flask","done": True },
]

def next_id():
    return max((task["id"] for task in tasks), default=0) + 1

#GET
@app.route("/tasks", methods=["GET"])
def get_tasks():
    #Lista todas as tarefas.
    return jsonify(tasks), 200 #Ok


#POST
@app.route("/tasks", methods=["POST"])
def create_task():
    #Adiciona uma nova tarefa.
    if not request.is_json:
        abort(400, description="Body must be JSON.")

    data = request.get_json()

    
    if "title" not in data:
        abort(400, description=" 'title'field is mandatory!")

    task = {
        "id": next_id(),
        "title": data["title"],
        "done": bool(data.get("done", False)),
    }
    tasks.append(task)
    return jsonify(task), 201 #Created


#PUT
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Edita uma tarefa existente."""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        abort(404, description="Task not found.")

    if not request.is_json:
        abort(400, description="Body must be JSON.")
    data = request.get_json()

    # Atualiza apenas campos enviados
    if "title" in data:
        task["title"] = data["title"]
    if "done" in data:
        task["done"] = bool(data["done"])

    return jsonify(task), 200 #Ok

#DELETE
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    #Apaga uma tarefa.
    index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)
    if index is None:
        abort(404, description="Task not found.")

    tasks.pop(index)
    return "No Content", 204 #No Content


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
