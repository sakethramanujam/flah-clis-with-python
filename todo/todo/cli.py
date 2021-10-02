import click
from .operations.main import add_task, showtasks

@click.group()
def cli():
    """
    Todo App for the command line
    """

@cli.group()
def todo():
    """
    Manages the todo cli
    """

@todo.command("add")
@click.argument("desc")
def add(desc):
    add_task(desc)
    click.echo(f"Task {desc} added to the list!")

@todo.command("show")
def show():
    showtasks()