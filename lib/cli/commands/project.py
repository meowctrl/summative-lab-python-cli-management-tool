from lib.cli.models.project import Project
from lib.cli.models.user import User
from rich.table import Table
from rich.console import Console

console = Console()

def list_projects(args):
    try:
        user = (User.get_by_email(args.user) or User.get_by_id(args.user)) if hasattr(args, "user") and args.user else None
        if hasattr(args, "user") and args.user and not user:
            console.print(f"[red]Error: User '{args.user}' not found[/red]")
            return
        projects = Project.get_by_owner(user.user_id) if user else Project.get_all()
        if not projects:
            console.print("[yellow]No projects found[/yellow]")
            return
        table = Table(title=f"Projects" + (f" ({user.name})" if user else ""))
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Tasks")
        for p in projects:
            table.add_row(p.project_id, p.name, p.status, str(len(p.tasks)))
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def setup_project_parser(subparsers):
    p = subparsers.add_parser("list-projects")
    p.add_argument("-u", "--user")
    p.set_defaults(func=list_projects)
