import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo " , key= "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events= True, size = [45,5])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box, add_button],[list_box,edit_button]],
                   font=('Helvetica',15))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case"Add":
            todos = functions.get_todos()
            new_todo =values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(value=todos)

        case "Edit":
            todos_to_edit = value['todos'][0]
            new_todo = value['todo']

            todos = functions.get_todos()
            index = todos.index(todos_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

        case 'todos':
            window['todo'].update(value=values['todos'])
        case sg.WIN_CLOSED:
            break

window.close()