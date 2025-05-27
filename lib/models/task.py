import sqlite3
from lib.models import DB_FILE

class Task:
    def __init__(self, title, description, user_id, completed=False, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.user_id = user_id

def save(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        if self.id:
            cursor.execute(
                """UPDATE tasks SET title=?, description=?, completed=?, user_id=?
                WHERE id=?""",
                (self.title, self.description, self.completed, self.user_id, self.id)
            )
        else:
            cursor.execute(
                """INSERT INTO tasks (title, description, completed, user_id)
                VALUES (?, ?, ?, ?)""",
                (self.title, self.description, self.completed, self.user_id)
            )
            self.id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        return self
