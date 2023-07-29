from functions import get_todos, write_todos
import PySimpleGUI as psg
import time

clock = psg.Text('', key='clock')
label = psg.Text("Type in a To-do:")
input_box = psg.InputText(tooltip='Enter a to-do item', key='todo')
list_box = psg.Listbox(values=get_todos(), key='todos', enable_events=True, size=(40, 10))
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")
app_gui = psg.Window(title='My To-Do App',
                     layout=[[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]
                             ],
                     font=('Helvetica', 15))
while True:
    event, values = app_gui.read(timeout=200)
    app_gui['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    selected_todos = values['todos']
    selected_todo = values['todo']
    match event:
        case "Add":
            try:
                new_todo = selected_todo.replace("\n", "") + "\n"
                if len(selected_todos) > 0 or selected_todo != '':
                    todos = get_todos()
                    print(todos)
                    todos.append(new_todo)
                    write_todos(todos)
                    print(todos)
                    app_gui['todos'].update(values=todos)
                    app_gui['todo'].update(value='')
                else:
                    psg.Popup('Please type an item first!', title='Error',
                              font=('Helvetica', 15), auto_close=True,
                              auto_close_duration=5)
            except IndexError:
                psg.Popup('There are no items in the list!', title='Error',
                          font=('Helvetica', 15), auto_close=True,
                          auto_close_duration=5)

        case "Edit":
            try:
                todo_to_edit = selected_todos[0]
                new_todo = selected_todo.replace("\n", "") + "\n"
                todos = get_todos()
                print(todos)
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                print(todos)
                app_gui['todos'].update(values=todos)
                app_gui['todo'].update(value='')
            except IndexError:
                psg.Popup('Please select an item first!', title='Error', font=('Helvetica', 15), auto_close=True, auto_close_duration=5)

        case "Complete":
            try:
                todo_to_complete = selected_todos[0]
                new_todo = selected_todo.replace("\n", "") + "\n"
                todos = get_todos()
                print(todos)
                index = todos.index(todo_to_complete)
                todos.remove(todos[index])
                write_todos(todos)
                print(todos)
                app_gui['todos'].update(values=todos)
                app_gui['todo'].update(value='')
            except IndexError:
                psg.Popup('Please select an item first!', title='Error', font=('Helvetica', 15), auto_close=True, auto_close_duration=5)

        case 'todos':
            try:
                app_gui['todo'].update(value=selected_todos[0])
            except IndexError:
                psg.Popup('There are no items in the list!', title='Error', font=('Helvetica', 15), auto_close=True, auto_close_duration=5)

        case "Exit":
            break

        case psg.WIN_CLOSED:
            break

app_gui.close()