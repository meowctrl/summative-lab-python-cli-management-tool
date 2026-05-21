"""File IO Configuration Guide."""

# File IO Features

The CLI Management Tool includes comprehensive JSON file persistence with error handling.

## Storage Module (cli/storage.py)

The `Storage` class handles all file IO operations:

- **Data Directory**: `data/` (auto-created if missing)
- **Files Created**:
  - `data/users.json` - User objects
  - `data/projects.json` - Project objects
  - `data/tasks.json` - Task objects

## Key Methods

```python
storage = Storage()

# Load data
storage.load_all()           # Load all data types
storage.load_users()         # Load only users
storage.load_projects()      # Load only projects
storage.load_tasks()         # Load only tasks

# Save data
storage.save_users(users)    # Save users
storage.save_projects(projects)  # Save projects
storage.save_tasks(tasks)    # Save tasks
storage.save_all(users, projects, tasks)  # Save everything
```

## Serialization (to_dict methods)

Each model class implements `to_dict()` for JSON serialization:

```python
user = User.create("John", "john@example.com")
user_dict = user.to_dict()  # Returns dict ready for JSON
```

## Error Handling

All file operations use try-except blocks:

- **Missing Files**: Returns empty list if file doesn't exist
- **Malformed JSON**: Catches `JSONDecodeError`, prints error, returns empty list
- **General Errors**: Catches all exceptions, prints descriptive message

Example error handling:
```python
try:
    data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error: Malformed JSON - {e}")
    return []
except Exception as e:
    print(f"Error loading data: {e}")
    return []
```

## Python Best Practices

✓ `if __name__ == "__main__"` guards in all executable modules
✓ Proper exception handling with specific error types
✓ Pathlib for cross-platform file paths
✓ ISO format for datetime serialization
✓ Default values for missing attributes

## Usage Example

```python
from cli.storage import Storage

storage = Storage()

# Load existing data
storage.load_all()

# Create objects
user = User.create("Alice", "alice@example.com")
project = Project.create("My Project", user.user_id)

# Save to disk
storage.save_all(User.get_all(), Project.get_all(), Task.get_all())
```

## Demo Script

Run `python demo.py` to see a complete example:
- Creates sample users, projects, and tasks
- Saves to JSON files
- Demonstrates error handling
- Loads and displays saved data
