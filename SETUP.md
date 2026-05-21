"""Installation guide for CLI Management Tool."""

# Setup & Installation

## Install Dependencies

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or manually install
pip install rich==0.13.0
```

## Package Information

### Rich (v0.13.0)

**Purpose**: Enhanced CLI output with colors, tables, and formatting

**Usage in Project**:
- Renders project lists as formatted tables
- Color-coded output (cyan, magenta, green, yellow, red)
- Better error messages and user feedback

**Features Used**:
- `rich.table.Table` - Display projects in tabular format
- `rich.console.Console` - Handle console output with styling

## Requirements.txt

The `requirements.txt` file lists all external dependencies:

```
rich==0.13.0
```

Pin specific versions for reproducible environments.

## Running the Application

```bash
# Using the CLI
python -m cli add-user alice -e alice@example.com
python -m cli list-projects
python -m cli complete-task TASK-3000

# Run demo
python demo.py
```

## Output Example

When running `list-projects`, you'll see:

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━┓
┃ Project ID  ┃ Name            ┃ Status ┃ Tasks ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━┩
│ PROJ-2000   │ Website Redesign│ active │ 2     │
│ PROJ-2001   │ Mobile App      │ active │ 1     │
└─────────────┴─────────────────┴────────┴───────┘
```

## Architecture

- **cli/commands/project.py** - Uses rich.table.Table for list-projects
- **cli/storage.py** - Handles JSON persistence
- **demo.py** - Demonstrates full workflow
