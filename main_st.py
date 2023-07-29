import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    local_todo = st.session_state['new_todo']
    todos.append(local_todo + "\n")
    write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")

st.subheader("This is my todo app")

st.write("The purpose of this app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo item:", label_visibility='hidden',
              placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')