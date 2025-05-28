#!/usr/bin/env python3

from lib.models import init_db
from helpers import TodoHelpers
from lib.models.todo import Todo

def test_crud_operations():
    
    print(" Testing CRUD Operations")
    print("=" * 30)
    
    
    init_db()
    
    
    print("\n1. Testing CREATE operation:")
    todo1 = TodoHelpers.create("Buy groceries")
    todo2 = TodoHelpers.create("Walk the dog")
    todo3 = TodoHelpers.create("Finish project")
    
    if todo1:
        print(f" Created: {todo1}")
    if todo2:
        print(f" Created: {todo2}")
    if todo3:
        print(f" Created: {todo3}")
    

    print("\n2. Testing READ operation (get all):")
    all_todos = TodoHelpers.get_all()
    for todo in all_todos:
        print(f" {todo}")
    
    
    print("\n3. Testing READ operation (find by ID):")
    if todo1:
        found_todo = TodoHelpers.find_by_id(todo1.id)
        if found_todo:
            print(f" Found: {found_todo}")
    
    
    print("\n4. Testing UPDATE operation (mark complete):")
    if todo1:
        updated_todo = TodoHelpers.mark_complete(todo1.id)
        if updated_todo:
            print(f" Completed: {updated_todo}")
    
    
    print("\n5. Testing UPDATE operation (change description):")
    if todo2:
        updated_todo = TodoHelpers.update(todo2.id, description="Walk the dog in the park")
        if updated_todo:
            print(f" Updated: {updated_todo}")
    
    
    print("\n6. Testing filtering by status:")
    pending_todos = TodoHelpers.get_pending()
    completed_todos = TodoHelpers.get_completed()
    
    print(f" Pending todos ({len(pending_todos)}):")
    for todo in pending_todos:
        print(f"   {todo}")
    
    print(f" Completed todos ({len(completed_todos)}):")
    for todo in completed_todos:
        print(f"   {todo}")
    
    
    print("\n7. Testing statistics:")
    total = TodoHelpers.count_all()
    pending = TodoHelpers.count_pending()
    completed = TodoHelpers.count_completed()
    
    print(f" Total: {total}, Pending: {pending}, Completed: {completed}")
    
    
    print("\n8. Testing DELETE operation:")
    if todo3:
        success = TodoHelpers.delete(todo3.id)
        if success:
            print(f"  Deleted todo with ID {todo3.id}")
    
    
    print("\n9. Final state:")
    final_todos = TodoHelpers.get_all()
    for todo in final_todos:
        print(f" {todo}")

def test_error_handling():
   
    print("\n Testing Error Handling")
    print("=" * 30)
    
    
    print("\n1. Testing find non-existent todo:")
    non_existent = TodoHelpers.find_by_id(9999)
    if non_existent is None:
        print(" Correctly returned None for non-existent todo")
    
    
    print("\n2. Testing update non-existent todo:")
    result = TodoHelpers.update(9999, description="This should fail")
    if result is None:
        print(" Correctly returned None for non-existent todo update")
    
    
    print("\n3. Testing delete non-existent todo:")
    result = TodoHelpers.delete(9999)
    if not result:
        print(" Correctly returned False for non-existent todo deletion")

def display_menu():
    
    print("\n Todo App Debug Menu")
    print("=" * 25)
    print("1. Test CRUD operations")
    print("2. Test error handling")
    print("3. Clear all todos")
    print("4. Add sample data")
    print("5. Show all todos")
    print("6. Exit")
    print("=" * 25)

def clear_all_todos():
    
    todos = TodoHelpers.get_all()
    count = 0
    for todo in todos:
        if TodoHelpers.delete(todo.id):
            count += 1
    print(f"  Cleared {count} todos")

def add_sample_data():
    
    sample_todos = [
        "Complete the todo app project",
        "Write unit tests",
        "Update documentation",
        "Review code",
        "Deploy to production"
    ]
    
    print(" Adding sample data...")
    for description in sample_todos:
        todo = TodoHelpers.create(description)
        if todo:
            print(f" Added: {todo}")
    
    
    todos = TodoHelpers.get_all()
    if len(todos) >= 2:
        TodoHelpers.mark_complete(todos[0].id)
        TodoHelpers.mark_complete(todos[1].id)
        print(" Marked first two todos as completed")

def show_all_todos():
    
    todos = TodoHelpers.get_all()
    if not todos:
        print(" No todos found")
        return
    
    print(f"\n All Todos ({len(todos)} total)")
    print("=" * 30)
    for todo in todos:
        print(todo)
    
    
    total = TodoHelpers.count_all()
    pending = TodoHelpers.count_pending()
    completed = TodoHelpers.count_completed()
    print(f"\n Stats: {total} total, {pending} pending, {completed} completed")

def main():
   
    init_db()
    
    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                test_crud_operations()
            elif choice == '2':
                test_error_handling()
            elif choice == '3':
                clear_all_todos()
            elif choice == '4':
                add_sample_data()
            elif choice == '5':
                show_all_todos()
            elif choice == '6':
                print(" Exiting debug mode")
                break
            else:
                print(" Invalid choice. Please select 1-6.")
                
        except KeyboardInterrupt:
            print("\n Exiting debug mode")
            break
        except Exception as e:
            print(f" Error: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()