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