import sqlite3
from lib.config import DB_FILE

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
    
    def delete(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_id(user_id):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return User(id=row[0], username=row[1], email=row[2])
        return None
    
    @staticmethod
    def get_all():
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()

        return [User(id=row[0], username=row[1], email=row[2]) for row in rows]
