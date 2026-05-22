def setup_user_parser(subparsers):
    """Setup user command parser"""
    user_parser = subparsers.add_parser("user", help="User commands")
    user_parser.set_defaults(func=lambda args: print("User command"))
