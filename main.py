from functions import get_todos, write_todos

user_prompt = "Enter a todo: "
filepath = 'todos.txt'

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(user_prompt)

            todos = get_todos()

            todos.append(todo+"\n")

            write_todos(todos)
        case 'show':
            todos = get_todos()

            todos = [todo.strip("\n") for todo in todos]

            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo}')
        case 'edit':
            todos = get_todos()
            number = int(input('Which todo do you want to edit? ')) - 1
            new_todo = input("Edit: ")

            todos[number] = new_todo + "\n"

            write_todos(todos)
        case 'complete':
            todos = get_todos()

            number = int(input('Which todo do you want to complete? ')) - 1

            todos.pop(number)

            write_todos(todos)
        case 'exit':
            break


print('Bye!')