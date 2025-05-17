import json, os

FILENAME = todos.json
prompt_main = input("Welcome to the Todo App! Press write add to continue...")
def main():
    if prompt_main == "add":
        list = input("Enter the items to add: ")
        with open('todos.json') as f:
            json.dump(todos, f)
    elseif prompt_main == "remove":
        remove = input("Enter the items to remove: ")
    elif prompt_main == "list":

