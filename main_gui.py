from functions import get_todos, write_todos
import PySimpleGUI as psg

label = psg.Text("Type n a To-do:")
input_box = psg.InputText(tooltip='Enter a to-do item')
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")
app_gui = psg.Window(title='My To-Do App', layout=[[label], [input_box, add_button], [edit_button, complete_button], [exit_button]])

app_gui.read()
app_gui.close()