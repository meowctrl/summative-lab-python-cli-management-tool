def setup_task_parser(subparsers):
    """Setup task command parser"""
    task_parser = subparsers.add_parser("task", help="Task commands")
    task_parser.set_defaults(func=lambda args: print("Task command"))
