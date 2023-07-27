from functions import get_todos, write_todos
import PySimpleGUI as psg

label = psg.Text("Type n a To-do:")
input_box = psg.InputText(tooltip='Enter a to-do item', key='todo')
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")
app_gui = psg.Window(title='My To-Do App',
                     layout=[[label],
                             [input_box, add_button],
                             [edit_button, complete_button],
                             [exit_button]],
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
        case "Exit":
            break
        case psg.WIN_CLOSED:
            break

app_gui.close()