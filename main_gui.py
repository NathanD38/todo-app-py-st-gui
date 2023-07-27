from functions import get_todos, write_todos
import PySimpleGUI as psg
# from datetime import datetime
#
# current_date = datetime.now()
# formatted_date = current_date.strftime('It is %b %d, %Y %H:%M:%S')
# print(formatted_date)

label = psg.Text("Type in a To-do:")
input_box = psg.InputText(tooltip='Enter a to-do item', key='todo')
list_box = psg.Listbox(values=get_todos(), key='todos', enable_events=True, size=(40, 10))
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")
app_gui = psg.Window(title='My To-Do App',
                     layout=[[label],
                             [input_box, add_button],
                             [list_box, edit_button],
                             [complete_button, exit_button]
                             ],
                     font=('Helvetica', 15))
while True:
    event, values = app_gui.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            app_gui['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            write_todos(todos)
            app_gui['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_complete)
            todos.remove(todos[index])
            write_todos(todos)
            app_gui['todos'].update(values=todos)
        case 'todos':
            app_gui['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case psg.WIN_CLOSED:
            break

app_gui.close()