from lib.helpers import create_user, create_task

def seed_database():
    
    user1 = create_user("brian_njoroge", "brian21@gmail.com")
    user2 = create_user("njuguna_njoroge", "njuguna@gmail.com")

    create_task("Buy groceries", "Milk, eggs, bread", user1.id)
    create_task("Finish project", "Complete the CLI todo app", user1.id)
    create_task("Call mom", "Sunday evening", user1.id)

    create_task("Schedule meeting", "With the design team", user2.id)
    create_task("Review PRs", "Code reviews for team", user2.id)

    print("Database seeded successfully!")