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
    show_tasks()
    return 0

def show_tasks(n:int=None):
    print("ID | Description | Status")
    print("-------------------------")
    tasks = read()
    for i,id in enumerate(tasks.keys()):
        if n and i==n:
            break
        print(f"{id} | {tasks.get(id)['desc']} | {tasks.get(id)['status']} ")
    return 0

def remove_task(taskid:str):
    alltasks=read()
    if taskid not in alltasks.keys():
        print("Task with specified id not found!")
        return 1
    del alltasks[taskid]
    print(f"Task:{taskid} has been now been deleted!")
    tasklist={"tasks":alltasks}
    write(tasklist=tasklist)
    show_tasks()
    return 0

def update_task(taskid:str, taskupdate:str):
    alltasks = read()
    if taskid not in alltasks.keys():
        print("Given task doesn't already exist in the list yet")
        return 1
    if not taskupdate:
        taskupdate =  alltasks[taskid]["desc"]
    alltasks[taskid]["desc"] = taskupdate
    tasklist={"tasks":alltasks}
    write(tasklist=tasklist)
    print(f"Task:{taskid} has been updated")
    show_tasks()
    return 0

def update_task_state(taskid:str, status:str):
    alltasks = read()
    if taskid not in alltasks.keys():
        print("Given task doesn't already exist in the list yet")
        return 1
    if not status:
        status =  alltasks[taskid]["status"]
    alltasks[taskid]["status"] = status
    tasklist={"tasks":alltasks}
    write(tasklist=tasklist)
    print(f"Task:{taskid} has been marked {status}")
    show_tasks()
    return 0
    

