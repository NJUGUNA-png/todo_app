import click
from helpers import TodoHelpers
from lib.models import init_db


init_db()

@click.group()
def cli():
    
    pass

@cli.command()
@click.argument('description')
def add(description):
    
    todo = TodoHelpers.create(description)
    if todo:
        click.echo(f" Added: {todo}")
    else:
        click.echo(" Failed to add todo")

@cli.command()
@click.option('--status', type=click.Choice(['all', 'pending', 'completed']), default='all', help='Filter by status')
def list(status):
    
    if status == 'pending':
        todos = TodoHelpers.get_pending()
        title = " Pending Todos"
    elif status == 'completed':
        todos = TodoHelpers.get_completed()
        title = " Completed Todos"
    else:
        todos = TodoHelpers.get_all()
        title = " All Todos"
    
    click.echo(f"\n{title}")
    click.echo("=" * len(title))
    
    if not todos:
        click.echo("No todos found.")
        return
    
    for todo in todos:
        click.echo(todo)
    
    
    total = TodoHelpers.count_all()
    pending = TodoHelpers.count_pending()
    completed = TodoHelpers.count_completed()
    
    click.echo(f"\n Summary: {total} total, {pending} pending, {completed} completed")

@cli.command()
@click.argument('todo_id', type=int)
def complete(todo_id):
   
    todo = TodoHelpers.mark_complete(todo_id)
    if todo:
        click.echo(f" Completed: {todo}")
    else:
        click.echo(f" Todo with ID {todo_id} not found")

@cli.command()
@click.argument('todo_id', type=int)
def incomplete(todo_id):
   
    todo = TodoHelpers.mark_incomplete(todo_id)
    if todo:
        click.echo(f" Marked incomplete: {todo}")
    else:
        click.echo(f" Todo with ID {todo_id} not found")

@cli.command()
@click.argument('todo_id', type=int)
@click.argument('description')
def update(todo_id, description):
    
    todo = TodoHelpers.update(todo_id, description=description)
    if todo:
        click.echo(f" Updated: {todo}")
    else:
        click.echo(f" Todo with ID {todo_id} not found")

@cli.command()
@click.argument('todo_id', type=int)
@click.confirmation_option(prompt='Are you sure you want to delete this todo?')
def delete(todo_id):
   
    success = TodoHelpers.delete(todo_id)
    if success:
        click.echo(f"  Deleted todo with ID {todo_id}")
    else:
        click.echo(f" Todo with ID {todo_id} not found")

@cli.command()
@click.argument('todo_id', type=int)
def show(todo_id):
    
    todo = TodoHelpers.find_by_id(todo_id)
    if todo:
        click.echo(f"\n📄 Todo Details:")
        click.echo(f"ID: {todo.id}")
        click.echo(f"Description: {todo.description}")
        click.echo(f"Status: {' Completed' if todo.completed else '⏳ Pending'}")
        click.echo(f"Created: {todo.created_at}")
        click.echo(f"Updated: {todo.updated_at}")
    else:
        click.echo(f" Todo with ID {todo_id} not found")

@cli.command()
def stats():
   
    total = TodoHelpers.count_all()
    pending = TodoHelpers.count_pending()
    completed = TodoHelpers.count_completed()
    
    click.echo(f"\n Todo Statistics")
    click.echo("=" * 20)
    click.echo(f"Total todos: {total}")
    click.echo(f"Pending: {pending}")
    click.echo(f"Completed: {completed}")
    
    if total > 0:
        completion_rate = (completed / total) * 100
        click.echo(f"Completion rate: {completion_rate:.1f}%")

@cli.command()
@click.confirmation_option(prompt='Are you sure you want to clear all completed todos?')
def clear_completed():
   
    completed_todos = TodoHelpers.get_completed()
    count = 0
    
    for todo in completed_todos:
        if TodoHelpers.delete(todo.id):
            count += 1
    
    click.echo(f"  Cleared {count} completed todos")

if __name__ == '__main__':
    cli()