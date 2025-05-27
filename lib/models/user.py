import sqlite3
from lib.models import DB_FILE

class User:
    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email