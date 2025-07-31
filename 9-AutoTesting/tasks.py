tasks = []

def get_all_tasks():
    return tasks

def add_task(data):
    if not data or "title" not in data or len(data["title"]) < 3:
        return False, "title inválido"
    if "done" not in data or not isinstance(data["done"], bool):
        return False, "done deve ser true ou false"

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": data["done"]
    }
    tasks.append(new_task)
    return True, new_task