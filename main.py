import json
import os

FILENAME = 'todos.json'

def load_todos():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []
def save_todos(todos):
    with open(FILENAME, 'w') as f:
        json.dump(todos, f)

def main():
    todos = load_todos()
    prompt_main = input("Welcome to the Todo App! Type add, remove, or list: ")
    if prompt_main == "add":
        item = input("Enter the item to add: ")
        todos.append(item)
        save_todos(todos)
    elif prompt_main == "remove":
        item = input("Enter the item to remove: ")
        if item in todos:
            todos.remove(item)
            save_todos(todos)
    elif prompt_main == "list":
        print("Your todos:", todos)
    main()

if __name__ == "__main__":
    main()