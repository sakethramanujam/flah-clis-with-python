import uuid
import click
from .todoio import read, write

def add_task(desc:str):
    if not desc:
        click.echo("Cannot add an empty task")
        
    tasks = read()
    task_id = str(uuid.uuid4()).split('-')[0]
    tasks[task_id]={'desc':desc,'status':'nope'}
    tasklist={"tasks":tasks}
    write(tasklist=tasklist)
    showtasks()
    return 0

def showtasks():
    print("ID | Description | Status")
    print("-------------------------")
    tasks = read()
    for id in tasks.keys():
        print(f"{id} | {tasks.get(id)['desc']} | {tasks.get(id)['status']} ")
    return 0

def remove_task(id:str):
    tasks=read()
    if id not in tasks.keys():
        print("Task with specified id not found!")
        return 1
    del tasks[id]
    tasklist={"tasks":read()}
    write(tasklist=tasklist)
    showtasks()
    return 0

def update_task(id:str):
    tasks=read()
    
