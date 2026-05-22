from cli.models.task import Task, TaskStatus
from cli.storage import Storage

storage = Storage()

def complete_task(args):
    try:
        task = Task.get_by_id(args.task_id)
        if not task:
            print(f"Error: Task '{args.task_id}' not found")
            return
        task.complete()
        print(f"✓ Task completed: {task}")
        storage.save_tasks(Task.get_all())
    except Exception as e:
        print(f"Error: {e}")

def setup_task_parser(subparsers):
    p = subparsers.add_parser("complete-task")
    p.add_argument("task_id")
    p.add_argument("-n", "--notes")
    p.set_defaults(func=complete_task)
