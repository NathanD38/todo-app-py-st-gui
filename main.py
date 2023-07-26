user_prompt = "Enter a todo: "
filepath = 'todos.txt'

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(user_prompt)

            with open(filepath) as file:
                todos = file.readlines()

            todos.append(todo+"\n")

            with open(filepath, 'w') as file:
                file.writelines(todos)
        case 'show':
            with open(filepath) as file:
                todos = file.readlines()

            todos = [todo.strip("\n") for todo in todos]

            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo}')
        case 'edit':
            with open(filepath) as file:
                todos = file.readlines()
            number = int(input('Which todo do you want to edit? ')) - 1
            new_todo = input("Edit: ")

            todos[number] = new_todo + "\n"

            with open(filepath, 'w') as file:
                file.writelines(todos)
        case 'complete':
            with open(filepath) as file:
                todos = file.readlines()

            number = int(input('Which todo do you want to complete? ')) - 1

            todos.pop(number)

            with open(filepath, 'w') as file:
                file.writelines(todos)
        case 'exit':
            break


print('Bye!')