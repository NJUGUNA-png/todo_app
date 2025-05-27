from lib.models.user import User
from lib.models.task import Task

def create_user(username, email):
    """Create a new user"""
    user = User(username=username, email=email)
    return user.save()

def get_all_users():
    """Get all users"""
    return User.get_all()
