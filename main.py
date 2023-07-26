user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(user_prompt)
            todos.append(todo)
        case 'show':
            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo}')
        case 'edit':
            number = int(input('Which todo do you want to edit? ')) - 1
            new_todo = input("Edit: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input('Which todo do you want to complete? ')) - 1
            todos.pop(number)
        case 'exit':
            break


print('Bye!')