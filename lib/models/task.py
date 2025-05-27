import sqlite3
from lib.models import DB_FILE

class Task:
    def __init__(self, title, description, user_id, completed=False, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.user_id = user_id