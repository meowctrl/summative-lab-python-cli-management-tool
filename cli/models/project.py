from datetime import datetime

class Project:
    _projects = {}
    _id_counter = 2000
    
    def __init__(self, name, owner_id, description="", project_id=None):
        self._project_id = project_id or f"PROJ-{Project._id_counter}"
        if not project_id:
            Project._id_counter += 1
        self._name = name
        self._owner_id = owner_id
        self._description = description
        self._created_at = datetime.now()
        self._tasks = []
        self._status = "active"
    
    @property
    def project_id(self):
        return self._project_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def owner_id(self):
        return self._owner_id
    
    @property
    def description(self):
        return self._description
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def tasks(self):
        return self._tasks
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value in ["active", "completed", "archived"]:
            self._status = value
    
    def to_dict(self):
        return {"project_id": self.project_id, "name": self.name, "owner_id": self.owner_id, "description": self.description, "status": self.status, "created_at": self.created_at.isoformat(), "tasks": self.tasks}
    
    def __str__(self):
        return f"{self.name} ({self.project_id}) - {self.status}"
    
    @classmethod
    def create(cls, name, owner_id, description=""):
        p = cls(name, owner_id, description)
        cls._projects[p.project_id] = p
        return p
    
    @classmethod
    def get_by_id(cls, project_id):
        return cls._projects.get(project_id)
    
    @classmethod
    def get_by_owner(cls, owner_id):
        return [p for p in cls._projects.values() if p.owner_id == owner_id]
    
    @classmethod
    def get_all(cls):
        return list(cls._projects.values())
    
    @classmethod
    def delete(cls, project_id):
        return cls._projects.pop(project_id, None) is not None
    
    @classmethod
    def clear_all(cls):
        cls._projects.clear()
