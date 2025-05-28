from lib.models import create_tables
from lib.models.user import User
from lib.models.task import Task
from lib.helpers import *

def test_application():
    print("Testing database connection...")
    create_tables()
    print("Database tables created successfully!")