import click
from .operations.main import (add_task, show_tasks,
                              update_task, remove_task,
                              update_task_state)


@ click.group()
def cli():
    """
    Todo App made in Python, for the command line \n
    Go Devils!
    """


@ cli.command("add", help="Add a task to the list, example: td add 'do this'")
@ click.argument("desc", type=str)
def add(desc):
    add_task(desc)
    click.echo(f"Task {desc} added to the list!")


@ cli.command("show", help="Displays all the tasks in the list example: td show")
@ click.option("-n", "-n-tasks", type=int, help="Optional Argument to show only a particular number of tasks")
def show(n):
    show_tasks(n)


@ cli.command("del", help="Delete a task from the list by passing it's id example: td del -tid abcdef")
@click.argument("taskid")
@ click.option("-tid", "--taskid", type=str,
               help="id of the task to be deleted, run `td show` to find out the id")
def delete(taskid):
    if not taskid:
        print("Cannot pass an empty id")
        return 1
    remove_task(taskid=taskid)
    return 0


@ cli.group("update", help="Update a given task using it's id")
def update():
    pass


@ update.command("task")
@ click.option("-tid", "--taskid", type=str,
               help="id of the task to be updated, run `td show` to find out the id")
@ click.option("-t", "--task",
               help="Task description to be edited")
def modify_task_desc(taskid, task):
    if not taskid:
        print("Cannot pass an empty id")
        return 1
    update_task(taskid=taskid, taskupdate=task)
    return 0


@ update.command("status")
@ click.option("-tid", "--taskid", type=str,
               help="id of the task to be updated, run `td show` to find out the id")
@ click.option("-s", "--status",
               help="New status of the task")
def modify_task_status(taskid, status):
    if not taskid:
        print("Taskid cannot be empty!")
        return 1
    update_task_state(taskid=taskid, status=status)
    return 0
