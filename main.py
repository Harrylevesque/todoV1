from prompt_toolkit.shortcuts import checkboxlist_dialog
import json
import os
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import checkboxlist_dialog

style = Style.from_dict({
    "dialog": "bg:#282c34",
    "dialog frame.label": "bg:#61afef #282c34",
    "checkbox": "#abb2bf",
    "checkbox-checked": "bg:#98c379 #282c34",
    "button": "bg:#61afef #282c34",
    "button.focused": "bg:#e06c75 #282c34",
})

FILENAME = 'todos.json'

def load_todos():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

todos = load_todos()
choices = [(todo, todo) for todo in todos]
result = checkboxlist_dialog(
    title="Todo List",
    text="Use arrows to move, space to toggle, enter to finish.",
    values=choices,
    style=style
).run()

def save_todos(todos):
    with open(FILENAME, 'w') as f:
        json.dump(todos, f)

def main():
    todos = load_todos()
    # Prepare choices as (value, label)
    choices = [(todo, todo) for todo in todos]
    result = checkboxlist_dialog(
        title="Todo List",
        text="Use arrows to move, space to toggle, enter to finish.",
        values=choices
    ).run()
    if result is not None:
        print("Checked items:", result)

if __name__ == "__main__":
    main()