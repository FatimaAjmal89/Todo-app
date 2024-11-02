import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo " , key= "todo")
add_button = sg.Button("Add")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")

list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events= True, size = [30,5])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box, add_button],[list_box,edit_button,complete_button, exit_button]],
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
            window['todos'].update(values=todos)

        case "Edit":
            todos_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todos_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()