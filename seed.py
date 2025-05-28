#!/usr/bin/env python3


from lib.models import init_db
from helpers import TodoHelpers

def seed_database():
    
    print("🌱 Seeding database...")
    
    
    init_db()
    print("✅ Database initialized")
    
    
    sample_todos = [
        {
            "description": "Set up development environment",
            "completed": True
        },
        {
            "description": "Create database models",
            "completed": True
        },
        {
            "description": "Implement CRUD operations",
            "completed": True
        },
        {
            "description": "Build CLI interface",
            "completed": False
        },
        {
            "description": "Write unit tests",
            "completed": False
        },
        {
            "description": "Add error handling",
            "completed": False
        },
        {
            "description": "Create documentation",
            "completed": False
        },
        {
            "description": "Deploy application",
            "completed": False
        },
        {
            "description": "Buy groceries for the week",
            "completed": False
        },
        {
            "description": "Schedule dentist appointment",
            "completed": False
        },
        {
            "description": "Read 30 minutes daily",
            "completed": True
        },
        {
            "description": "Exercise for 45 minutes",
            "completed": False
        },
        {
            "description": "Call mom and dad",
            "completed": True
        },
        {
            "description": "Organize home office",
            "completed": False
        },
        {
            "description": "Pay monthly bills",
            "completed": True
        }
    ]
    
    
    existing_todos = TodoHelpers.get_all()
    if existing_todos:
        response = input(f"Database already contains {len(existing_todos)} todos. Do you want to clear them first? (y/N): ")
        if response.lower() in ['y', 'yes']:
            print("🗑️  Clearing existing todos...")
            for todo in existing_todos:
                TodoHelpers.delete(todo.id)
            print("✅ Existing todos cleared")
    
    
    print("📝 Adding sample todos...")
    added_count = 0
    
    for todo_data in sample_todos:
        todo = TodoHelpers.create(todo_data["description"])
        if todo:
            
            if todo_data["completed"]:
                TodoHelpers.mark_complete(todo.id)
            added_count += 1
            status = "✅" if todo_data["completed"] else "⏳"
            print(f"   {status} {todo.description}")
    
    print(f"\n🎉 Successfully added {added_count} sample todos!")
    
    
    total = TodoHelpers.count_all()
    pending = TodoHelpers.count_pending()
    completed = TodoHelpers.count_completed()
    
    print(f"\n📊 Database Statistics:")
    print(f"   Total todos: {total}")
    print(f"   Pending: {pending}")
    print(f"   Completed: {completed}")
    
    if total > 0:
        completion_rate = (completed / total) * 100
        print(f"   Completion rate: {completion_rate:.1f}%")
    
    print("\n🚀 Database seeded successfully!")
    print("You can now run the application with: python cli.py")

def reset_database():
   
    print("🔄 Resetting database...")
    
    
    existing_todos = TodoHelpers.get_all()
    if existing_todos:
        print(f"🗑️  Clearing {len(existing_todos)} existing todos...")
        for todo in existing_todos:
            TodoHelpers.delete(todo.id)
    
    
    init_db()
    print("✅ Database reset complete!")

def main():
    
    print("🌱 Todo App Database Seeder")
    print("=" * 30)
    print("1. Seed database with sample data")
    print("2. Reset database (clear all data)")
    print("3. Exit")
    print("=" * 30)
    
    try:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            seed_database()
        elif choice == '2':
            confirm = input("Are you sure you want to reset the database? This will delete all todos! (y/N): ")
            if confirm.lower() in ['y', 'yes']:
                reset_database()
            else:
                print("❌ Reset cancelled")
        elif choice == '3':
            print("👋 Goodbye!")
        else:
            print("❌ Invalid choice. Please select 1-3.")
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()