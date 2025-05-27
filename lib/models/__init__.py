import sqlite3
from .user import User
from .task import Task

DB_FILE = "todo.db"

def create_tables():
    """Create database tables"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()