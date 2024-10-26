import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type  add ,show,complete,or exit:  ")
    user_action = user_action.strip()
    # we adding add buttom
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("enter new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid ")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue


    elif 'exit' in user_action:
        break
    else:
        print("unvalid commad")

print("byeeeee bhagoo")
