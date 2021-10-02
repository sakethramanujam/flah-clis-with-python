import click
from .operations.main import (add_task, show_tasks,
                              update_task, remove_task,
                              update_task_state)


@click.group()
def cli():
    """
    Todo App made in Python, for the command line \n
    Go Devils!
    """


# Add show tasks command
# Add add tasks command
# Add delete task command
# Add update task command
# Add update status command