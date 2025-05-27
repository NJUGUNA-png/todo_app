from lib.models.user import User
from lib.models.task import Task

def create_user(username, email):
    
    user = User(username=username, email=email)
    return user.save()

def get_all_users():
    
    return User.get_all()

def find_user_by_id(user_id):
    
    return User.find_by_id(user_id)

def create_task(title, description, user_id):

    task = Task(title=title, description=description, user_id=user_id)
    return task.save()

def get_all_tasks():
    
    return Task.get_all()

def get_user_tasks(user_id):
    
    return Task.get_by_user(user_id)

def find_task_by_id(task_id):
    
    return Task.find_by_id(task_id)

def update_task(task_id, title=None, description=None, completed=None):
    
    task = Task.find_by_id(task_id)
    if not task:
        return None
    
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if completed is not None:
        task.completed = completed
    
    return task.save()

def delete_task(task_id):
    
    task = Task.find_by_id(task_id)
    if task:
        task.delete()
        return True
    return False

def toggle_task_complete(task_id):
    
    task = Task.find_by_id(task_id)
    if task:
        task.toggle_complete()
        return task
    return None
