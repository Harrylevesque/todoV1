import json, os

FILENAME = todos
prompt_main = input("Welcome to the Todo App! Press write add to continue...")
list = []
def main():
    if prompt_main == "add":
        list = input("Enter the items to add: ")
    elseif prompt_main == "remove":
        remove = input("Enter the items to remove: ")
    elif prompt_main == "list":
        prin
