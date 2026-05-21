from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Task:
    _tasks = {}
    _id_counter = 3000
    
    def __init__(self, title, project_id, assigned_to=None, description="", task_id=None):
        self._task_id = task_id or f"TASK-{Task._id_counter}"
        if not task_id:
            Task._id_counter += 1
        self._title = title
        self._project_id = project_id
        self._assigned_to = assigned_to
        self._description = description
        self._status = TaskStatus.PENDING
        self._created_at = datetime.now()
        self._completed_at = None
    
    @property
    def task_id(self):
        return self._task_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def project_id(self):
        return self._project_id
    
    @property
    def assigned_to(self):
        return self._assigned_to
    
    @property
    def description(self):
        return self._description
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if isinstance(value, TaskStatus):
            self._status = value
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def completed_at(self):
        return self._completed_at
    
    def complete(self, notes=None):
        self.status = TaskStatus.COMPLETED
        self._completed_at = datetime.now()
    
    def to_dict(self):
        return {"task_id": self.task_id, "title": self.title, "project_id": self.project_id, "assigned_to": self.assigned_to, "description": self.description, "status": self.status.value, "created_at": self.created_at.isoformat(), "completed_at": self.completed_at.isoformat() if self.completed_at else None}
    
    def __str__(self):
        assigned = f" → {self.assigned_to}" if self.assigned_to else ""
        return f"{self.task_id}: {self.title} [{self.status.value}]{assigned}"
    
    @classmethod
    def create(cls, title, project_id, assigned_to=None, description=""):
        task = cls(title, project_id, assigned_to, description)
        cls._tasks[task.task_id] = task
        return task
    
    @classmethod
    def get_by_id(cls, task_id):
        return cls._tasks.get(task_id)
    
    @classmethod
    def get_by_project(cls, project_id):
        return [t for t in cls._tasks.values() if t.project_id == project_id]
    
    @classmethod
    def get_by_assignee(cls, user_id):
        return [t for t in cls._tasks.values() if t.assigned_to == user_id]
    
    @classmethod
    def get_all(cls):
        return list(cls._tasks.values())
    
    @classmethod
    def delete(cls, task_id):
        return cls._tasks.pop(task_id, None) is not None
    
    @classmethod
    def clear_all(cls):
        cls._tasks.clear()
