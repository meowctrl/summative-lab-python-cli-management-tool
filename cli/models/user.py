from cli.models.base import Person

class User(Person):
    _users = {}
    _id_counter = 1000
    
    def __init__(self, name, email, user_id=None):
        super().__init__(name, email)
        self._user_id = user_id or f"USER-{User._id_counter}"
        if not user_id:
            User._id_counter += 1
        self._projects = []
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def projects(self):
        return self._projects
    
    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "email": self.email, "created_at": self.created_at.isoformat(), "projects": self.projects}
    
    def __str__(self):
        return f"{self.name} ({self.user_id}) - {self.email}"
    
    @classmethod
    def create(cls, name, email):
        user = cls(name, email)
        cls._users[user.user_id] = user
        return user
    
    @classmethod
    def get_by_id(cls, user_id):
        return cls._users.get(user_id)
    
    @classmethod
    def get_by_email(cls, email):
        return next((u for u in cls._users.values() if u.email == email), None)
    
    @classmethod
    def get_all(cls):
        return list(cls._users.values())
    
    @classmethod
    def delete(cls, user_id):
        return cls._users.pop(user_id, None) is not None
    
    @classmethod
    def clear_all(cls):
        cls._users.clear()
