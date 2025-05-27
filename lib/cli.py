import click
from lib.helpers import (
    create_user, get_all_users, find_user_by_id,
    create_task, get_user_tasks, find_task_by_id,
    update_task, delete_task, toggle_task_complete
)

@click.group()
def cli():
    
    pass


@cli.command()
@click.option('--username', prompt=True, help="User's username")
@click.option('--email', prompt=True, help="User's email")
def add_user(username, email):
    
    user = create_user(username, email)
    click.echo(f"User created: {user.username} (ID: {user.id})")

@cli.command()
def list_users():
    
    users = get_all_users()
    for user in users:
        click.echo(f"{user.id}: {user.username} - {user.email}")

@cli.command()
@click.option('--user-id', prompt=True, type=int, help="User ID")
@click.option('--title', prompt=True, help="Task title")
@click.option('--description', prompt=True, help="Task description")
def add_task(user_id, title, description):
    """Add a new task"""
    user = find_user_by_id(user_id)
    if not user:
        click.echo("User not found!")
        return
    
    task = create_task(title, description, user_id)
    click.echo(f"Task created: {task.title} (ID: {task.id})")
