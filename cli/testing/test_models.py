import pytest
from cli.models.task import Task
from cli.models.user import User

def test_task_creation():
    Task.clear_all()
    task = Task("Write tests")
    assert task.title == "Write tests"
    assert task.status.value == "pending"

def test_task_complete():
    Task.clear_all()
    task = Task("Write tests")
    task.complete()
    assert task.status.value == "completed"

def test_user_creation():
    User.clear_all()
    user = User("Alice", "alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"

def test_user_get_all():
    User.clear_all()
    user1 = User.create("Alice", "alice@example.com")
    user2 = User.create("Bob", "bob@example.com")
    assert len(User.get_all()) == 2

def test_user_get_by_email():
    User.clear_all()
    user = User.create("Alice", "alice@example.com")
    found = User.get_by_email("alice@example.com")
    assert found == user

def test_user_get_by_email_not_found():
    User.clear_all()
    found = User.get_by_email("missing@example.com")
    assert found == None
    