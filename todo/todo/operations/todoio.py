import os
import json
import tempfile

tempdir = tempfile.gettempdir()
todofp = os.path.join(tempdir, "todo.json")
existing_file_name = ""


def _todo_exists(todofp: str = todofp):
    """
    Check if the todo.json file exists in the temporary files directory
    """
    if not os.path.isfile(todofp):
        create_todo(todofp=todofp)


def create_todo(todofp: str = todofp):
    """
    Create a todo.json file in a specified path
    """
    template = {"tasks": {}}
    with open(todofp, 'w') as f:
        f.write(json.dumps(template))


def read(todofp: str = todofp):
    """
    open tasks json file and return all tasks
    """
    _todo_exists(todofp=todofp)
    tasks = json.load(open(todofp, 'r')).get('tasks')
    return tasks


def write(tasklist: dict, todofp: str = todofp):
    try:
        with open(todofp, 'w') as f:
            f.write(json.dumps(tasklist))
        return 0
    except Exception as e:
        print(f"Error {e} occured when updating tasks!")
        return 1




    