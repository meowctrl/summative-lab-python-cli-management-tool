import pytest
from lib.cli.models.task import Task
from lib.cli.models.user import User

def test_task_creation():
    task = Task("Write tests")
    assert task.title == "Write tests"
    assert task.completed == False

def test_task_complete():
    task = Task("Write tests")
    task.complete()
    assert task.completed == True

def test_user_creation():
    user = User("Alice")
    assert user.name == "Alice"
    assert len(user.tasks) == 0

def test_user_add_task():
    user = User("Alice")
    task = Task("Write tests")
    user.add_task(task)
    assert len(user.tasks) == 1
    assert user.tasks[0].title == "Write tests"

def test_user_get_task_by_title():
    user = User("Alice")
    task = Task("Write tests")
    user.add_task(task)
    found = user.get_task_by_title("Write tests")
    assert found == task

def test_user_get_task_not_found():
    user = User("Alice")
    found = user.get_task_by_title("Missing")
    assert found == None