from flask import Flask,jsonify, request, abort
app = Flask(__name__)
tasks =[]

def next_id():
    return 1+max([task["id"] for task in tasks],default=0)

#GET
@app.route("/tasks",methods=["GET"])
def get_task():
    return jsonify(tasks),200

#POST
@app.route("/tasks",methods=["POST"])
def add_task():
    data = request.get_json()

    #Title Validation
    if "title" not in data or not isinstance(data["title"],str) or len(data["title"].strip()) < 3:
        return jsonify({"error":"Mandatory 'title' or at least 3 characters."}),412
    
    #done status validation
    if "done" not in data or not isinstance(data["done"],bool):
        return jsonify({"error": "'done' state is mandatory, it must be true or false."}),412
    #Passing Validations
    task= {
        "id":next_id(),
        "title":data["title"].strip(),
        "done": data["done"]
    }
    tasks.append(task)
    return jsonify(task), 201

#PUT
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def put_task(task_id):
    #Edita uma tarefa existente
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

    return jsonify(task), 200

#DELETE
@app.route("/tasks/<int:task_id>",methods=["DELETE"])
def del_task(task_id):
    index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)
    if index is None:
        abort(404, description="Task not found.")

    tasks.pop(index)
    return "No Content", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)