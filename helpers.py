from lib.models import get_session
from lib.models.todo import Todo
from sqlalchemy.exc import SQLAlchemyError

class TodoHelpers:
   
    
    @staticmethod
    def get_all():
        
        session = get_session()
        try:
            todos = session.query(Todo).order_by(Todo.created_at.desc()).all()
            return todos
        except SQLAlchemyError as e:
            print(f"Error fetching todos: {e}")
            return []
        finally:
            session.close()
    
    @staticmethod
    def find_by_id(todo_id):
       
        session = get_session()
        try:
            todo = session.query(Todo).filter(Todo.id == todo_id).first()
            return todo
        except SQLAlchemyError as e:
            print(f"Error finding todo: {e}")
            return None
        finally:
            session.close()
    
    @staticmethod
    def create(description):
       
        session = get_session()
        try:
            todo = Todo(description=description)
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating todo: {e}")
            return None
        finally:
            session.close()
    
    @staticmethod
    def update(todo_id, description=None, completed=None):
       
        session = get_session()
        try:
            todo = session.query(Todo).filter(Todo.id == todo_id).first()
            if not todo:
                return None
            
            if description is not None:
                todo.description = description
            if completed is not None:
                todo.completed = completed
            
            session.commit()
            session.refresh(todo)
            return todo
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating todo: {e}")
            return None
        finally:
            session.close()
    
    @staticmethod
    def delete(todo_id):
        
        session = get_session()
        try:
            todo = session.query(Todo).filter(Todo.id == todo_id).first()
            if not todo:
                return False
            
            session.delete(todo)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting todo: {e}")
            return False
        finally:
            session.close()
    
    @staticmethod
    def get_by_status(completed=False):
       
        session = get_session()
        try:
            todos = session.query(Todo).filter(Todo.completed == completed).order_by(Todo.created_at.desc()).all()
            return todos
        except SQLAlchemyError as e:
            print(f"Error fetching todos by status: {e}")
            return []
        finally:
            session.close()
    
    @staticmethod
    def get_pending():
        
        return TodoHelpers.get_by_status(completed=False)
    
    @staticmethod
    def get_completed():
        
        return TodoHelpers.get_by_status(completed=True)
    
    @staticmethod
    def mark_complete(todo_id):
       
        return TodoHelpers.update(todo_id, completed=True)
    
    @staticmethod
    def mark_incomplete(todo_id):

        return TodoHelpers.update(todo_id, completed=False)
    
    @staticmethod
    def count_all():
        
        session = get_session()
        try:
            count = session.query(Todo).count()
            return count
        except SQLAlchemyError as e:
            print(f"Error counting todos: {e}")
            return 0
        finally:
            session.close()
    
    @staticmethod
    def count_pending():
        
        session = get_session()
        try:
            count = session.query(Todo).filter(Todo.completed == False).count()
            return count
        except SQLAlchemyError as e:
            print(f"Error counting pending todos: {e}")
            return 0
        finally:
            session.close()
    
    @staticmethod
    def count_completed():
       
        session = get_session()
        try:
            count = session.query(Todo).filter(Todo.completed == True).count()
            return count
        except SQLAlchemyError as e:
            print(f"Error counting completed todos: {e}")
            return 0
        finally:
            session.close()