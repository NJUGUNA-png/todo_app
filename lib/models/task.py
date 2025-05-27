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

def delete(self):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (self.id,))
    conn.commit()
    conn.close()

def toggle_complete(self):
    self.completed = not self.completed
    self.save()
    
@staticmethod
def find_by_id(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return Task(
            id=row[0],
            title=row[1],
            description=row[2],
            completed=bool(row[3]),
            user_id=row[4]
        )
    return None

@staticmethod
def get_all():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        Task(
            id=row[0],
            title=row[1],
            description=row[2],
            completed=bool(row[3]),
            user_id=row[4]
        ) for row in rows
    ]

@staticmethod
def get_by_user(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
        