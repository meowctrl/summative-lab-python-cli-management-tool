from datetime import datetime

class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._created_at = datetime.now()
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value and isinstance(value, str):
            self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" in value:
            self._email = value
    
    @property
    def created_at(self):
        return self._created_at
