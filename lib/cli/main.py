import argparse, sys
from lib.cli.commands.user import setup_user_parser
from lib.cli.commands.project import setup_project_parser
from lib.cli.commands.task import setup_task_parser
from lib.cli.storage import Storage

storage = Storage()

def create_parser():
    p = argparse.ArgumentParser(prog="cli-tool")
    p.add_argument("-v", "--version", action="version", version="1.0.0")
    s = p.add_subparsers(dest="command")
    setup_user_parser(s)
    setup_project_parser(s)
    setup_task_parser(s)
    return p

def main():
    parser = create_parser()
    args = parser.parse_args()
    storage.load_all()
    if not hasattr(args, "func"):
        parser.print_help()
        return
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()

