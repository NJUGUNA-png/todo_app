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