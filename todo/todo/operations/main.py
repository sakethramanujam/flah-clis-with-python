import uuid
from .todoio import read, write

def add_task(desc:str):
    if not desc:
        return "Cannot add an empty task"
    tasks = read()
    task_id = str(uuid.uuid4()).split('-')[0]
    tasks[task_id]={'desc':desc,'status':'nope'}
    tasklist={"tasks":tasks}
    write(tasklist=tasklist)
    showtasks()

def showtasks():
    print("ID | Description | Status")
    print("-------------------------")
    tasks = read()
    for id in tasks.keys():
        print(f"{id} | {tasks.get(id)['desc']} | {tasks.get(id)['status']} ")
    

   