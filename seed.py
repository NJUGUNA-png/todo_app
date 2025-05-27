from lib.helpers import create_user, create_task

def seed_database():
    """Seed the database with sample data"""
    
    user1 = create_user("brian_njoroge", "brian21@gmail.com")
    user2 = create_user("njuguna_njoroge", "njuguna@gmail.com")
