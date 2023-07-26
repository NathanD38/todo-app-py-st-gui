filepath = 'todos.txt'


def get_todos():
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def write_todos(todos):
    with open(filepath, 'w') as file:
        file.writelines(todos)