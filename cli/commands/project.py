def setup_project_parser(subparsers):
    """Setup project command parser"""
    project_parser = subparsers.add_parser("project", help="Project commands")
    project_parser.set_defaults(func=lambda args: print("Project command"))
