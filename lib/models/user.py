import sqlite3
from lib.models import DB_FILE

class User:
    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email

        def save(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        if self.id:
            cursor.execute(
                "UPDATE users SET username=?, email=? WHERE id=?",
                (self.username, self.email, self.id)
            )
        else:
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (?, ?)",
                (self.username, self.email)
            )
            self.id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        return self