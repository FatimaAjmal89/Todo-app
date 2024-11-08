FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """read a text file and return the list of
    to-do items.
    """
    with open(FILEPATH, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg , filepath=FILEPATH ):
    """write the to-do item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# this just for experiment
if __name__ == "__main__":
    print(("hi"))