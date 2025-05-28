from lib.models import create_tables
from lib.models.user import User
from lib.models.task import Task
from lib.helpers import *

def test_application():
    print("Testing database connection...")
    create_tables()
    print("Database tables created successfully!")

    print("\nTesting user creation...")
    user = create_user("test_user", "test@example.com")
    print(f"Created user: {user.username} (ID: {user.id})")

    print("\nTesting task creation...")
    task = create_task("Test task", "This is a test task", user.id)
    print(f"Created task: {task.title} (ID: {task.id})")

    print("\nTesting task completion toggle...")
    task = toggle_task_complete(task.id)
    print(f"Task completed status: {task.completed}")

    print("\nTesting task update...")
    task = update_task(task.id, title="Updated test task")
    print(f"Updated task title: {task.title}")

    print("\nTesting task deletion...")
    if delete_task(task.id):
        print("Task deleted successfully")

    print("\nTesting user deletion...")
    user = find_user_by_id(user.id)
    user.delete()
    print("User deleted successfully")
    