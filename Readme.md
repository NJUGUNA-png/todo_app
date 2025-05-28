# Todo App

A command-line todo application built with Python, SQLAlchemy, and Click.

## Features

- Add new todos
- List all todos
- Mark todos as complete/incomplete
- Delete todos
- Update todo descriptions
- Filter todos by status

## Installation

1. Install pipenv if you haven't already:
   ```bash
   pip install pipenv
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Initialize the database:
   ```bash
   python seed.py
   ```

## Usage

Run the application:
```bash
python cli.py
```

### Available Commands

- `python cli.py add "Task description"` - Add a new todo
- `python cli.py list` - List all todos
- `python cli.py list --status pending` - List pending todos
- `python cli.py list --status completed` - List completed todos
- `python cli.py complete <id>` - Mark todo as complete
- `python cli.py incomplete <id>` - Mark todo as incomplete
- `python cli.py update <id> "New description"` - Update todo description
- `python cli.py delete <id>` - Delete a todo

## Database

The app uses SQLite database (`todos.db`) to store todo items.

## Development

- Run `python debug.py` to test the application during development
- Database models are in `lib/models/`
- Helper functions are in `helpers.py`