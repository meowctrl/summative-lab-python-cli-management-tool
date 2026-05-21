from lib.cli.models.user import User
from lib.cli.storage import Storage

storage = Storage()

def add_user(args):
    try:
        if User.get_by_email(args.email):
            print(f"Error: User with email '{args.email}' already exists")
            return
        user = User.create(args.name, args.email)
        print(f"✓ User created: {user}")
        storage.save_users(User.get_all())
    except Exception as e:
        print(f"Error: {e}")

def setup_user_parser(subparsers):
    p = subparsers.add_parser("add-user")
    p.add_argument("name")
    p.add_argument("-e", "--email", required=True)
    p.set_defaults(func=add_user)
