from functions import get_todos, write_todos

user_prompt = "Enter a todo: "
actions = ['Add', 'Show', 'Edit', 'Complete', 'Exit']

while True:
    user_action = input("Type Add, Show, Edit, Complete, or Exit: ")
    user_action = user_action.strip().capitalize()

    if user_action in actions:
        match user_action:
            case 'Add':
                todo = input(user_prompt)

                todos = get_todos()

                todos.append(todo+"\n")

                write_todos(todos)
            case 'Show':
                todos = get_todos()

                todos = [todo.strip("\n") for todo in todos]

                for index, todo in enumerate(todos):
                    print(f'{index+1}-{todo.capitalize()}')
            case 'Edit':
                todos = get_todos()
                number = int(input('Which todo do you want to edit? ')) - 1
                new_todo = input("Edit: ")

                todos[number] = new_todo + "\n"

                write_todos(todos)
            case 'Complete':
                todos = get_todos()

                number = int(input('Which todo do you want to complete? ')) - 1

                todos.pop(number)

                write_todos(todos)
            case 'Exit':
                break
    else:
        print('Wrong input! Try again!')


print('Bye!')