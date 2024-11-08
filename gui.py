import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGrey14")

clock = sg.Text('', key = 'clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo " , key= "todo")
add_button = sg.Button("Add", size=10)
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")
edit_button = sg.Button("Edit")

list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events= True, size = [30,7])


window = sg.Window('My To-Do App',
                   layout=[[clock],[label],[input_box, add_button],[list_box,edit_button,complete_button, exit_button]],
                   font=('Helvetica',15))

while True:
    event,values = window.read(timeout=200)
    window["clock"].update(value= time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case"Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:

                todos_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todos_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!!", font =("Halvetica", 15))

        case "complete":
              try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
              except IndexError:
                  sg.popup("Please select an item first!!",font =("Halvetica", 15))


        case "exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()