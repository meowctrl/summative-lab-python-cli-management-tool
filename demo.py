"""Demo script showing CLI usage with file IO."""

import sys
from lib.cli.models.user import User
from lib.cli.models.project import Project
from lib.cli.models.task import Task
from lib.cli.storage import Storage


def demo():
    """Run a demonstration of the CLI tool."""
    storage = Storage()
    
    print("=" * 60)
    print("CLI Management Tool - File IO Demo")
    print("=" * 60)
    
    try:
        # Load existing data
        print("\n1. Loading data from storage...")
        storage.load_all()
        print(f"   Loaded {len(User.get_all())} users")
        print(f"   Loaded {len(Project.get_all())} projects")
        print(f"   Loaded {len(Task.get_all())} tasks")
        
        # Create users
        print("\n2. Creating users...")
        user1 = User.create("Alice Johnson", "alice@example.com")
        user2 = User.create("Bob Smith", "bob@example.com")
        print(f"   Created: {user1}")
        print(f"   Created: {user2}")
        
        # Create projects
        print("\n3. Creating projects...")
        proj1 = Project.create("Website Redesign", user1.user_id, "Modernize company website")
        proj2 = Project.create("Mobile App", user2.user_id, "Build iOS app")
        print(f"   Created: {proj1}")
        print(f"   Created: {proj2}")
        
        # Create tasks
        print("\n4. Creating tasks...")
        task1 = Task.create("Design homepage", proj1.project_id, user1.user_id, "Create mockups")
        task2 = Task.create("Set up database", proj1.project_id, user1.user_id)
        task3 = Task.create("Build API", proj2.project_id, user2.user_id)
        print(f"   Created: {task1}")
        print(f"   Created: {task2}")
        print(f"   Created: {task3}")
        
        # Complete a task
        print("\n5. Completing a task...")
        task1.complete("Mockups approved by stakeholders")
        print(f"   Updated: {task1}")
        
        # Save all data
        print("\n6. Saving data to JSON files...")
        storage.save_all(User.get_all(), Project.get_all(), Task.get_all())
        print("   ✓ Users saved to data/users.json")
        print("   ✓ Projects saved to data/projects.json")
        print("   ✓ Tasks saved to data/tasks.json")
        
        # Display summary
        print("\n7. Data Summary:")
        print(f"   Total Users: {len(User.get_all())}")
        print(f"   Total Projects: {len(Project.get_all())}")
        print(f"   Total Tasks: {len(Task.get_all())}")
        
        print("\n" + "=" * 60)
        print("Demo completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(demo())
