import json
from pathlib import Path

class Storage:
    DATA_DIR = Path("data")
    
    def __init__(self):
        self.DATA_DIR.mkdir(exist_ok=True)
    
    def _save(self, filename, data):
        try:
            with open(self.DATA_DIR / filename, "w") as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            print(f"Error saving {filename}: {e}")
    
    def _load(self, filename):
        try:
            filepath = self.DATA_DIR / filename
            if not filepath.exists():
                return []
            with open(filepath) as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Malformed JSON in {filename}")
            return []
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return []
    
    def save_users(self, users):
        self._save("users.json", [u.to_dict() for u in users])
    
    def load_users(self):
        from lib.cli.models.user import User
        users = []
        for item in self._load("users.json"):
            user = User(item["name"], item["email"], item["user_id"])
            User._users[user.user_id] = user
            users.append(user)
        return users
    
    def save_projects(self, projects):
        self._save("projects.json", [p.to_dict() for p in projects])
    
    def load_projects(self):
        from lib.cli.models.project import Project
        projects = []
        for item in self._load("projects.json"):
            p = Project(item["name"], item["owner_id"], item["description"], item["project_id"])
            Project._projects[p.project_id] = p
            projects.append(p)
        return projects
    
    def save_tasks(self, tasks):
        self._save("tasks.json", [t.to_dict() for t in tasks])
    
    def load_tasks(self):
        from lib.cli.models.task import Task, TaskStatus
        tasks = []
        for item in self._load("tasks.json"):
            t = Task(item["title"], item["project_id"], item.get("assigned_to"), item.get("description", ""), item["task_id"])
            t._status = TaskStatus(item["status"])
            Task._tasks[t.task_id] = t
            tasks.append(t)
        return tasks
    
    def load_all(self):
        self.load_users()
        self.load_projects()
        self.load_tasks()
    
    def save_all(self, users, projects, tasks):
        self.save_users(users)
        self.save_projects(projects)
        self.save_tasks(tasks)
